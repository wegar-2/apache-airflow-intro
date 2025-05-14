# Run DAG Test Inside Scheduler Container

Start by entering the scheduler container by running:

```commandline
docker exec -it apache-airflow-intro-airflow-scheduler-1 /bin/bash
```

Once you are in, the prompt should look like:
```commandline
airflow@1108b1409868:/opt/airflow$
```

To get help, run anything followed by the `-h` flag, e.g.:
```commandline
airflow -h
```

You can then unfurl the commands by looking at the help's description.


In order to do a test run of DAG `user_processing` run:
```commandline
airflow dags test user_processing 
```

To exit the container just run:
```commandline
exit
```
