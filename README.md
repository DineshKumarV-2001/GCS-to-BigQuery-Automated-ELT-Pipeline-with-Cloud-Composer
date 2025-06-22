# 📌 GCS to BigQuery Automated ELT Pipeline with Cloud Composer

## 🔹 Project Description:
Designed and implemented an automated ELT pipeline using Google Cloud services to ingest, transform, and load data efficiently. Leveraged Cloud Composer (Apache Airflow) for orchestration, enabling scheduled data movement from Google Cloud Storage (GCS) to BigQuery with transformation logic applied dynamically.

## 🔹 Tools & Technologies Used:
Google Cloud Storage (GCS), BigQuery, Cloud Composer, Apache Airflow, Python, SQL, IAM Roles, Firewall Configuration

## 🔹 Project Architecture:

![image](https://github.com/user-attachments/assets/d93b8c02-9b30-4295-929c-cc122a8ec585)


## 🔹 Key Highlights:

Developed a Cloud Composer DAG to automate the ELT process end-to-end.

Ingested country-wise CSV files from Google Cloud Storage (GCS) to BigQuery raw tables.

Created BigQuery external and internal tables from GCS source files using SQL.

Performed data transformation inside BigQuery, storing results in separate transformed tables per country.

Built BigQuery views for each country to simplify analytical querying.

Enabled Airflow web UI access by configuring GCP firewall rules and allowing port 8080.

Handled Airflow environment setup on Compute Engine, including Python package installations and Composer troubleshooting.

Focused on ELT approach: Extraction & Load from GCS ➝ Transform using SQL in BigQuery.

## Orchestration Executed Successfully

![Screenshot 2025-06-22 144607](https://github.com/user-attachments/assets/ba8e21a0-8e87-4840-8cce-e8bca2437535)



