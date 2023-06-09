from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator 

# from dags.subdags.subdag_downloads import subdag_downloads
from subdags.subdag_downloads import subdag_downloads

from datetime import datetime


with DAG(
    dag_id="group_dag_2",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:
    
    args = {
        "start_date": dag.start_date, 
        "schedule_interval": dag.schedule_interval,
        "catchup": dag.catchup
    }

    # IMPORTANT: the parameters of the parent DAG (here: dag) and the child DAG (here: downloads - dag returned by SubDagOperator to which subdag_downloads
    # method is passed) have to be the same --- cf. args dictionary defined above! 

    downloads = SubDagOperator(
        task_id="downloads",
        subdag=subdag_downloads(
            parent_dag_id=dag.dag_id,
            child_dag_id="downloads",
            args=args
        )
    )

    check_files = BashOperator(
        task_id="check_files",
        bash_command="sleep 10"
    )

    transform_a = BashOperator(
        task_id="transform_a",
        bash_command="sleep 10"
    )
    transform_b = BashOperator(
        task_id="transform_b",
        bash_command="sleep 10"
    )
    transform_c = BashOperator(
        task_id="transform_c",
        bash_command="sleep 10"
    )

    downloads >> check_files >> [transform_a, transform_b, transform_c]

