# Airflow Architecture

According to the [official docs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/overview.html) the key components of Airflow are:

1. *Webserver* - essentially, the GUI you can use to navigate Airflow
2. *Folder for DAG Files* - i.e. [this](../dags) folder
3. *Metadata database* -  
4. *Scheduler* - it has two key tasks: (a) schedules whole workflows and (b) submits component tasks 
	of the workflows to the *Executor*
5. *Executor* - its main purpose is (as mentioned above) running of the tasks that make up the workflows

Picture is worth a thousand words - and [documentation provides one to illustrate the relationships between the various components listed above](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/overview.html):

![airflow_architecture.png](./airflow_architecture.png)

