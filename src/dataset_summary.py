from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Dataset Summary").getOrCreate()

train_df = spark.read.option("sep", "\t").option("header", True).option("inferSchema", True).csv("local_data/drugLibTrain_raw.tsv")
test_df = spark.read.option("sep", "\t").option("header", True).option("inferSchema", True).csv("local_data/drugLibTest_raw.tsv")

total_rows = train_df.count() + test_df.count()

print("\n========== Dataset Summary ==========")
print(f"Training Reviews: {train_df.count():,}")
print(f"Test Reviews: {test_df.count():,}")
print(f"Total Reviews: {total_rows:,}")
print(f"Columns: {len(train_df.columns)}")
print("Column Names:")
for c in train_df.columns:
    print(f"- {c}")

print("\nSchema:")
train_df.printSchema()
print("====================================\n")

spark.stop()