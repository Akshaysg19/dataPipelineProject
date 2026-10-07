from pyspark.sql import functions as F


def clean_data(df):

    # Remove rows where country is NULL
    df = df.dropna(subset=["country"])

    # Replace NULL directors
    df = df.fillna({
        "director": "Unknown",
        "cast": "Unknown"
    })

    # Keep valid duration values
    df = df.filter(
        F.col("duration").rlike(r"^\d+ (min|Seasons?)$")
    )

    return df