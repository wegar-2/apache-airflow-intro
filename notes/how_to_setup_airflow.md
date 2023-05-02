# How to Setup Airflow

Firstly, download [this file](https://airflow.apache.org/docs/apache-airflow/2.6.0/docker-compose.yaml) and save it in a folder, say `my_airflow`. This file is a Docker Compose file. The file linked to here is to the version associated with Airflow 2.6.0. You might want to go to the [official Airflow site](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#running-airflow-in-docker) to get the most up-to-date version of this file. 

Moreover, you need to create a `.env` file in the `my_airflow` directory with the following content:

```
AIRFLOW_UID=50000
```


Then, open the terminal, `cd` to the folder containing the file mentioned above and run the following command: 

```
docker-compose up -d
```


If you encounter errors, you probably have to walk carefully through the official [Airflow guide on this topic](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#running-airflow-in-docker)
