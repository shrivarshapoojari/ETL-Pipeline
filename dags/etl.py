from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.decorators import task
from airflow.providers.postgres import PostgresHook
from airflow.utils.dates import days_ago
import json

with DAG(
    dag_id="nasa_apod_postgres",
    start_date=days_ago(1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
  #create table if not exists

  @task
  def create_table():
    postgres_hook=PostgresHook()

    create_table_query="""
    CREATE TABLE IF NOT EXISTS nasa_apod (  
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    explanation TEXT,
    url TEXT,
    date DATE ,
    media_type VARCHA(50)
    )
    
    """

   


  # Extract NASA API DATA
  extract_apod=SimpleHttpOperator(
    task_id="extract_apod",
    http_conn_id="nasa_api",
    endpoint="planetary/apod"
    method='GET',
    data={"api_key":"{{conn.nasa_api.extra_dejson.api_key}}"}
    response_filter=lambda response:response.json()
    
  )


  # Transform JSON DATA



  #Load the data to postgres


  #verify 


