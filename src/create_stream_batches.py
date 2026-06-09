from pyspark.sql import SparkSession
import os
import shutil

spark = SparkSession.builder \
    .appName("Create Streaming Batches") \
    .getOrCreate()

df = spark.read.parquet("outputs/cleaned_drug_reviews.parquet")

output_dir = "stream_input"

if os.path.exists(output_dir):
    shutil.rmtree(output_dir)

os.makedirs(output_dir, exist_ok=True)

# Split data into small batches
sample_df = df.select(
    "drug_name",
    "condition_clean",
    "rating",
    "effectiveness",
    "sideEffects",
    "review_length",
    "positive_review"
).limit(500)

batches = sample_df.randomSplit([0.2, 0.2, 0.2, 0.2, 0.2], seed=42)

for i, batch in enumerate(batches):
    batch.coalesce(1).write.mode("overwrite").csv(
        f"{output_dir}/batch_{i+1}",
        header=True
    )

print("Streaming batch files created in stream_input/")

spark.stop()