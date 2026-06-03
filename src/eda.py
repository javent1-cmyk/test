from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count, desc, asc
import os

spark = SparkSession.builder \
    .appName("Drug Review EDA") \
    .getOrCreate()

df = spark.read.parquet(
    "outputs/cleaned_drug_reviews.parquet"
)

os.makedirs("outputs/eda", exist_ok=True)

print("Cleaned Data Schema:")
df.printSchema()

# Question 1: Which drugs have the highest average satisfaction ratings?
top_drugs = (
    df.groupBy("drug_name")
      .agg(
          avg("rating").alias("avg_rating"),
          count("*").alias("review_count")
      )
      .orderBy(desc("avg_rating"))
)

top_drugs.show(20)

top_drugs.coalesce(1).write.mode("overwrite").csv(
    "outputs/eda/top_drugs",
    header=True
)

# Question 2: Which drugs have the lowest average satisfaction ratings?
bottom_drugs = (
    df.groupBy("drug_name")
      .agg(
          avg("rating").alias("avg_rating"),
          count("*").alias("review_count")
      )
      .orderBy(asc("avg_rating"))
)

bottom_drugs.show(20)

bottom_drugs.coalesce(1).write.mode("overwrite").csv(
    "outputs/eda/bottom_drugs",
    header=True
)

# Question 3: Which medical conditions have the highest average satisfaction ratings?
condition_ratings = (
    df.groupBy("condition_clean")
      .agg(
          avg("rating").alias("avg_rating"),
          count("*").alias("review_count")
      )
      .orderBy(desc("avg_rating"))
)

condition_ratings.show(20)

condition_ratings.coalesce(1).write.mode("overwrite").csv(
    "outputs/eda/condition_ratings",
    header=True
)

# Question 4: What is the rating distribution?
rating_distribution = (
    df.groupBy("rating")
      .agg(count("*").alias("review_count"))
      .orderBy("rating")
)

rating_distribution.show()

rating_distribution.coalesce(1).write.mode("overwrite").csv(
    "outputs/eda/rating_distribution",
    header=True
)

# Question 5: Do positive and negative reviews differ by review length?
review_length_analysis = (
    df.groupBy("positive_review")
      .agg(
          avg("review_length").alias("avg_review_length"),
          count("*").alias("review_count")
      )
      .orderBy("positive_review")
)

review_length_analysis.show()

review_length_analysis.coalesce(1).write.mode("overwrite").csv(
    "outputs/eda/review_length_analysis",
    header=True
)

# Save summary notes
with open("outputs/eda/eda_summary.txt", "w") as f:
    f.write("Drug Review Dataset EDA Summary\n")
    f.write("================================\n\n")
    f.write(f"Total cleaned rows: {df.count()}\n")
    f.write(f"Total columns: {len(df.columns)}\n\n")
    f.write("EDA outputs generated:\n")
    f.write("- top_drugs\n")
    f.write("- bottom_drugs\n")
    f.write("- condition_ratings\n")
    f.write("- rating_distribution\n")
    f.write("- review_length_analysis\n")

spark.stop()