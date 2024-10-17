import os
import sys
from datetime import datetime

from airflow import DAG
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pipelines import reddit_pipeline


from airflow.operators.python import PythonOperator



default_args={
    'owner': 'Atharv Nanaware',
    'start date':datetime(2024,10,16)
}

file_postfix = datetime.now().strftime("%Y%m%d")


dag=DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval="@daily",
    catchup= False,
    tags=['reddit','etl','pipeline']
)


#  Exgtract from reddit

# extraction from reddit
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    dag=dag
)

# upload to s3
upload_s3 = PythonOperator(
    task_id='s3_upload',
    python_callable=upload_s3_pipeline,
    dag=dag
)

extract >> upload_s3