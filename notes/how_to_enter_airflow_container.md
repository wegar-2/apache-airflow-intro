# How to Enter Airflow Container?


Start by running the following command:

```
docker compose ps -a
```


Expected output is:

```
XXXXXXYYYYYYYYY airflow_course_materials % docker compose ps -a
NAME                                           IMAGE                  COMMAND                  SERVICE             CREATED             STATUS                      PORTS
airflow_course_materials-airflow-init-1        apache/airflow:2.4.2   "/bin/bash -c 'funct…"   airflow-init        27 minutes ago      Exited (0) 25 minutes ago   
airflow_course_materials-airflow-scheduler-1   apache/airflow:2.4.2   "/usr/bin/dumb-init …"   airflow-scheduler   27 minutes ago      Up 25 minutes (healthy)     8080/tcp
airflow_course_materials-airflow-triggerer-1   apache/airflow:2.4.2   "/usr/bin/dumb-init …"   airflow-triggerer   27 minutes ago      Up 25 minutes (healthy)     8080/tcp
airflow_course_materials-airflow-webserver-1   apache/airflow:2.4.2   "/usr/bin/dumb-init …"   airflow-webserver   27 minutes ago      Up 25 minutes (healthy)     0.0.0.0:8080->8080/tcp
airflow_course_materials-airflow-worker-1      apache/airflow:2.4.2   "/usr/bin/dumb-init …"   airflow-worker      27 minutes ago      Up 25 minutes (healthy)     8080/tcp
airflow_course_materials-postgres-1            postgres:13            "docker-entrypoint.s…"   postgres            27 minutes ago      Up 27 minutes (healthy)     5432/tcp
airflow_course_materials-redis-1               redis:latest           "docker-entrypoint.s…"   redis               27 minutes ago      Up 27 minutes (healthy)     6379/tcp
```

In order to enter the worker, i.e. the `airflow_course_materials-airflow-worker-1` use the command:

```
docker exec -it airflow_course_materials-airflow-worker-1 /bin/bash
```

Note that you can enter a scheduler container analogously, that is 
by running:
```commandline
docker exec -it airflow_course_materials-airflow-scheduler-1 /bin/bash
```
