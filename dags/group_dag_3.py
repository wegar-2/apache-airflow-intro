from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator 

from subdags.subdag_downloads import subdag_downloads
from subdags.subdag_transforms import subdag_transforms

from datetime import datetime


with DAG(
    dag_id="group_dag_3",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:
    
    args = {
        "start_date": dag.start_date, 
        "schedule_interval": dag.schedule_interval,
        "catchup": dag.catchup
    }

    downloads = SubDagOperator(
        task_id="downloads",
        subdag=subdag_downloads(
            parent_dag_id=dag.dag_id,
            child_dag_id="downloads",
            args=args
        )
    )

    transforms = SubDagOperator(
        task_id="transforms",
        subdag=subdag_transforms(
            parent_dag_id=dag.dag_id,
            child_dag_id="transforms",
            args=args
        )
    )    


    check_files = BashOperator(
        task_id="check_files",
        bash_command="sleep 10"
    )

    downloads >> check_files >> transforms
