# 📌 GCS to BigQuery Automated ELT Pipeline with Cloud Composer

## 🔹 Project Description:
Designed and implemented an automated ELT pipeline using Google Cloud services to ingest, transform, and load data efficiently. Leveraged Cloud Composer (Apache Airflow) for orchestration, enabling scheduled data movement from Google Cloud Storage (GCS) to BigQuery with transformation logic applied dynamically.

## 🔹 Tools & Technologies Used:
Google Cloud Storage (GCS), BigQuery, Cloud Composer, Apache Airflow, Python, SQL, IAM Roles, Firewall Configuration

## 🔹 Key Highlights:

Developed DAGs in Apache Airflow to automate the ELT pipeline.

Configured GCS bucket as a raw data source and BigQuery as the data warehouse.

Handled schema creation and transformations using SQL within BigQuery.

Implemented country-wise data transformation using SQL views.

Set up necessary IAM policies, service accounts, and firewall rules to allow access via Compute Engine and enable Airflow web UI (port 8080).

Performed data aggregation queries to extract insights grouped by demographic (age group, country, etc.).

Scheduled daily runs to simulate continuous pipeline automation.
