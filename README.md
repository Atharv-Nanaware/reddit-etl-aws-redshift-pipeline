Reddit Data Pipeline Engineering | AWS End-to-End Data Engineering :

Overview 

    This project provides a comprehensive data pipeline solution that leverages AWS services and other modern tools to extract, transform, and load (ETL) Reddit data into a Redshift data warehouse for analytics and querying.

The pipeline is designed to:

    Extract data from Reddit using its API.
    Store the raw data into an Amazon S3 bucket using Apache Airflow.
    Transform the data using AWS Glue and Amazon Athena.
    Load the transformed data into Amazon Redshift for analytics and querying.
    Tools & Technologies

The following technologies are used to build the pipeline:

    Apache Airflow: Workflow orchestration and scheduling.
    Celery & PostgreSQL: For distributed task execution and metadata management in Airflow.
    Docker: Containerization for Airflow environment.
    Reddit API: Data extraction.
    AWS Glue: Data transformation.
    Amazon S3: Raw data storage.
    AWS Athena: Querying data stored in S3.
    Amazon Redshift: Data warehousing for analytics.

Project Structure;
    airflow_dags/: Contains Airflow DAGs for scheduling and orchestrating the ETL process.
    scripts/: Python scripts to interact with Reddit API and push data to S3.
    glue_jobs/: AWS Glue scripts for transforming the raw data.
    sql_queries/: SQL queries for Redshift analytics.
    docker-compose.yml: Configuration file for Docker setup.

