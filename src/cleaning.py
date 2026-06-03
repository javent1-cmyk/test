from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, when, lower, trim
import os

spark = SparkSession.builder \
    .appName("Drug Review Cleaning") \
    .getOrCreate()

train_df = spark.read.csv(
    "local_data/drugLibTrain_raw.tsv",
    sep="\t",
    header=True,
    inferSchema=True
)

test_df = spark.read.csv(
    "local_data/drugLibTest_raw.tsv",
    sep="\t",
    header=True,
    inferSchema=True
)

df = train_df.union(test_df)

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# Basic cleaning
clean_df = df \
    .dropDuplicates() \
    .withColumn("drug_name", lower(trim(col("urlDrugName")))) \
    .withColumn("condition_clean", lower(trim(col("condition")))) \
    .withColumn("review_length", length(col("commentsReview"))) \
    .withColumn(
        "positive_review",
        when(col("rating") >= 7, 1).otherwise(0)
    )

# Drop rows missing key fields
clean_df = clean_df.na.drop(subset=[
    "drug_name",
    "condition_clean",
    "rating",
    "effectiveness",
    "sideEffects",
    "commentsReview"
])

# Print verification
print(f"Original Rows: {df.count()}")
print(f"Cleaned Rows: {clean_df.count()}")

clean_df.printSchema()
clean_df.show(5)

# Save cleaned schema
with open("outputs/cleaned_schema.txt", "w") as f:
    f.write(f"Original Rows: {df.count()}\n")
    f.write(f"Cleaned Rows: {clean_df.count()}\n\n")
    f.write("Cleaned Schema:\n")
    f.write(clean_df._jdf.schema().treeString())

# Save cleaned data locally as parquet
clean_df.write.mode("overwrite").parquet("outputs/cleaned_drug_reviews.parquet")

spark.stop()