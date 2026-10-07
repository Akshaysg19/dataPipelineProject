from pyspark.sql import functions as F


def content_by_year(df):

    return (
        df.groupBy("release_year", "type")
          .agg(
              F.count("*").alias("title_count")
          )
          .orderBy("release_year", "type")
    )


def content_by_type(df):

    return (
        df.groupBy("type")
          .agg(
              F.count("*").alias("title_count")
          )
          .orderBy(F.desc("title_count"))
    )


def content_by_rating(df):

    return (
        df.groupBy("rating")
          .agg(
              F.count("*").alias("title_count")
          )
          .orderBy(F.desc("title_count"))
    )


def content_by_country(df):

    return (
        df.groupBy("country")
          .agg(
              F.count("*").alias("title_count")
          )
          .orderBy(F.desc("title_count"))
    )


def genre_summary(df):

    return (
        df.groupBy("first_genre")
          .agg(
              F.count("*").alias("title_count")
          )
          .orderBy(F.desc("title_count"))
    )