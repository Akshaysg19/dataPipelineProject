from datetime import datetime
import subprocess

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator


PROJECT_PATH = "/opt/airflow"
PIPELINE_PATH = "/opt/airflow/src/pipeline.py"


def run_netflix_pipeline():
    print("Starting Netflix PySpark pipeline...")

    result = subprocess.run(
        ["python", PIPELINE_PATH],
        cwd=PROJECT_PATH,
        capture_output=True,
        text=True
    )

    print("Pipeline output:")
    print(result.stdout)

    if result.stderr:
        print("Pipeline errors/warnings:")
        print(result.stderr)

    if result.returncode != 0:
        raise RuntimeError(
            f"Netflix pipeline failed with exit code {result.returncode}"
        )

    print("Netflix PySpark pipeline completed successfully!")


with DAG(
    dag_id="netflix_pipeline",
    start_date=datetime(2026, 10, 1),
    schedule=None,
    catchup=False,
    tags=["netflix", "pyspark", "data-engineering"],
) as dag:

    run_pipeline = PythonOperator(
        task_id="run_netflix_pipeline",
        python_callable=run_netflix_pipeline,
    )