# ETL Pipeline Project

This project implements an ETL (Extract, Transform, Load) pipeline using Apache Airflow to fetch and store NASA's Astronomy Picture of the Day (APOD) data into a PostgreSQL database.

## Project Structure

```
.
├── dags/
│   └── etl.py              # Main ETL DAG for NASA APOD data processing
├── include/                # Additional project files
├── plugins/                # Custom Airflow plugins
├── tests/
│   └── dags/
│       └── test_dag_example.py  # Test files for DAGs
├── Dockerfile              # Docker image configuration using Astronomer Runtime
├── docker-compose.yml      # Docker Compose for PostgreSQL database
├── requirements.txt        # Python dependencies
├── packages.txt            # System-level packages
├── airflow_settings.yaml   # Airflow configuration for connections and variables
└── README.md               
```