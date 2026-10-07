from pyspark.sql import functions as F


def transform_data(df):

    # Duration in minutes
    df = df.withColumn(
        "duration_minutes",
        F.when(
            F.col("duration").endswith("min"),
            F.regexp_extract(
                "duration",
                r"(\d+)",
                1
            ).cast("int")
        )
    )

    # First genre
    df = df.withColumn(
        "first_genre",
        F.trim(
            F.split(
                F.col("listed_in"),
                ","
            ).getItem(0)
        )
    )

    # Uppercase title
    df = df.withColumn(
        "title_upper",
        F.upper(F.col("title"))
    )

    return df