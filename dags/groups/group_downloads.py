from airflow.utils.task_group import TaskGroup
from airflow.operators.bash import BashOperator


def download_tasks():

    with TaskGroup("download_tasks_example", tooltip="download_tasks_example") as group:
        pass

        download_a = BashOperator(
            task_id="download_a", bash_command="sleep 10"
        )
        download_b = BashOperator(
            task_id="download_b", bash_command="sleep 10"
        )
        download_c = BashOperator(
            task_id="download_c", bash_command="sleep 10"
        )   

        return group

