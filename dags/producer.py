from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import datetime
 
my_file = Dataset("/tmp/my_file.txt")
another_file = Dataset("/tmp/another_file.txt")

with DAG(
    dag_id="producer",
    schedule="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False
):
    pass

    @task(outlets=[my_file])
    def update_dataset():
        with open(my_file.uri, "a+") as f:
            f.write("producer update")

    @task(outlets=[another_file])
    def update_another_dataset():
        with open(another_file.uri, "a+") as f:
            f.write("another producer update")

    update_dataset()
    update_another_dataset()

 