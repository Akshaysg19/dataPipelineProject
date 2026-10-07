from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("ReadSilver")
    .master("local[*]")
    .getOrCreate()
)

df = spark.read.parquet("output/silver/netflix")

df.printSchema()

df.select(
    "title",
    "type",
    "duration",
    "duration_minutes",
    "first_genre"
).show(10, truncate=False)