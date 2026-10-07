from pyspark.sql import SparkSession


def create_spark_session():
    return (
        SparkSession.builder
        .appName("NetflixDataPipeline")
        .master("local[*]")
        .getOrCreate()
    )