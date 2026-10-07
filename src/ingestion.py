from pyspark.sql import DataFrame


def read_netflix_data(spark, path: str) -> DataFrame:

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .option("multiLine", True)
        .option("quote", '"')
        .option("escape", '"')
        .csv(path)
    )

    return df