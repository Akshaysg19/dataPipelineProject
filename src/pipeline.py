from spark_session import create_spark_session
from ingestion import read_netflix_data
from cleaning import clean_data
from transformations import transform_data

from gold_transformations import (
    content_by_year,
    content_by_type,
    content_by_rating,
    content_by_country,
    genre_summary
)


INPUT_PATH = "data/raw/netflix_titles.csv"

SILVER_PATH = "output/silver/netflix"

GOLD_PATH = "output/gold"


def main():

    spark = create_spark_session()

    print("Reading data...")

    df = read_netflix_data(
        spark,
        INPUT_PATH
    )

    print("Input count:", df.count())

    print("Cleaning data...")

    df = clean_data(df)

    print("Transforming data...")

    df = transform_data(df)

    print("Writing Silver data...")

    df.write \
        .mode("overwrite") \
        .parquet(SILVER_PATH)

    print("Creating Gold datasets...")

    year_df = content_by_year(df)

    type_df = content_by_type(df)

    rating_df = content_by_rating(df)

    country_df = content_by_country(df)

    genre_df = genre_summary(df)

    print("Writing Gold datasets...")

    year_df.write \
        .mode("overwrite") \
        .parquet(f"{GOLD_PATH}/content_by_year")

    type_df.write \
        .mode("overwrite") \
        .parquet(f"{GOLD_PATH}/content_by_type")

    rating_df.write \
        .mode("overwrite") \
        .parquet(f"{GOLD_PATH}/content_by_rating")

    country_df.write \
        .mode("overwrite") \
        .parquet(f"{GOLD_PATH}/content_by_country")

    genre_df.write \
        .mode("overwrite") \
        .parquet(f"{GOLD_PATH}/genre_summary")

    print("Gold layer completed!")

    spark.stop()


if __name__ == "__main__":
    main()