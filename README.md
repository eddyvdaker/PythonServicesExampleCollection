# Python Services Example Collection
This repository shows minimal examples for how many services can be setup (using Docker and Docker-Compose) and be accessed from Python. Each service is contained in it's own folder. Each folder contains at least a Docker-Compose file, a code file containg the Python code, and a Dockerfile that runs the Python code. So the general structure of each folder is:
```
.
├── <SERVICE_NAME>
│   ├── code.py
│   ├── docker-compose.yml
│   ├── Dockerfile
│   └── <OPTIONAL: README with additional details>
```

To run an example, go to the folder of the service you want to run (e.g. `./PostgreSQL`) and run the command `docker-compose up`.

## Services:
The table below shows a list of services that have examples in this repository.

| Service    | Folder     | Notes         |
| ---------- | ---------- | ------------- |
| PostgreSQL | PostgreSQL | Uses Psycopg2 |