from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime

my_file = Dataset("/tmp/my_file.txt")
another_file = Dataset("/tmp/another_file.txt")

with DAG(
    dag_id="consumer",
    schedule=[my_file, another_file],
    start_date=datetime(2023, 1, 1),
    catchup=False
):
    
    @task
    def read_dataset():
        with open(my_file.uri, "r") as f:
            print(f.read())

    @task
    def read_another_dataset():
        with open(another_file.uri, "r") as f:
            print(f.read())

    read_dataset()
    read_another_dataset()
