from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder \
    .appName("Drug Review Streaming") \
    .getOrCreate()

schema = StructType([
    StructField("drug_name", StringType(), True),
    StructField("condition_clean", StringType(), True),
    StructField("rating", IntegerType(), True),
    StructField("effectiveness", StringType(), True),
    StructField("sideEffects", StringType(), True),
    StructField("review_length", IntegerType(), True),
    StructField("positive_review", IntegerType(), True)
])

stream_df = spark.readStream \
    .schema(schema) \
    .option("header", True) \
    .csv("stream_input/*")

satisfaction_by_drug = (
    stream_df.groupBy("drug_name")
      .agg(
          avg("rating").alias("avg_rating"),
          count("*").alias("review_count")
      )
)

query = satisfaction_by_drug.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", False) \
    .option("checkpointLocation", "stream_checkpoint/drug_metrics") \
    .start()

query.awaitTermination(60)

spark.stop()