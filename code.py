from datetime import datetime
from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.providers.google.cloud.sensors.gcs import GCSObjectExistenceSensor  # ✅ Missing import fixed

# Default DAG arguments
default_args = {
    'owner': 'airflow',
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# List of countries to split into individual tables
country_list = [
    'China', 'Japan', 'UK', 'India'
]

# Define the DAG
with DAG(
    dag_id='elt_csv_gcs_to_bigquery_country_split',
    default_args=default_args,
    description='ELT Pipeline: GCS to BigQuery with Country-wise Split',
    schedule_interval=None,  # manual run
    start_date=datetime(2024, 6, 22),
    catchup=False,
    tags=['bigquery', 'gcs', 'elt', 'split_by_country'],
) as dag:

    # Task 1: Check for file existence in GCS
    check_file_exists = GCSObjectExistenceSensor(
        task_id='check_file_existence',
        bucket='you-bucket-name',
        object='global_health_data.csv',  # ✅ Typo fixed here (was `oject`)
        timeout=300,  # max wait: 5 mins
        poke_interval=30,
        mode='poke'
    )

    # Task 2: Load CSV from GCS into BigQuery staging table
    load_csv_to_bigquery = GCSToBigQueryOperator(
        task_id='load_csv_to_bq',
        bucket='you-bucket-name',
        source_objects=['dataset.csv'],
        destination_project_dataset_table='your-project-name.your-dataset.table-name',
        source_format='CSV',
        allow_jagged_rows=True,
        ignore_unknown_values=True,
        write_disposition='WRITE_TRUNCATE',
        skip_leading_rows=1,
        field_delimiter=',',
        autodetect=True,
    )

    # Task 3: Split into country-wise tables
    for country in country_list:
        country_table_name = country.replace(" ", "_")  # Sanitize table names

        split_task = BigQueryInsertJobOperator(
            task_id=f'split_{country_table_name.lower()}',
            configuration={
                "query": {
                    "query": f"""
                        CREATE OR REPLACE TABLE `your-project-name.new-dataset.{country_table_name}` AS
                        SELECT * FROM `your-project-name.your-dataset.table-name`    
                        WHERE Country = '{country}';
                    """,
                    "useLegacySql": False,
                }
            }
        )

        # Define task flow
        check_file_exists >> load_csv_to_bigquery >> split_task
