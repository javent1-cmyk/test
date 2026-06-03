# Data ingestion script placeholder
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Drug Review Ingestion") \
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

print(f"Total Rows: {df.count()}")
df.printSchema()
df.show(5)
import os 
os.makedirs("outputs", exist_ok=True)

with open("outputs/schema.txt", "w") as f:
    f.write(f"Total Rows: {df.count()}\n\n")
    f.write("Schema:\n")
    f.write(df._jdf.schema().treeString())


print(f"Total Rows: {df.count()}")

df.printSchema()

df.show(5)

spark.stop()