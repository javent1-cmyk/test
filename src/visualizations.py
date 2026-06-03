from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count, desc
import matplotlib.pyplot as plt
import os

spark = SparkSession.builder \
    .appName("Drug Review Visualizations") \
    .getOrCreate()

df = spark.read.parquet(
    "outputs/cleaned_drug_reviews.parquet"
)

os.makedirs("outputs/charts", exist_ok=True)

# Chart 1: Rating Distribution
rating_dist = (
    df.groupBy("rating")
      .count()
      .orderBy("rating")
)

pdf = rating_dist.toPandas()

plt.figure(figsize=(8, 5))
plt.bar(pdf["rating"], pdf["count"])
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Review Count")
plt.tight_layout()
plt.savefig("outputs/charts/rating_distribution.png")
plt.close()

# Chart 2: Most Reviewed Drugs
most_reviewed = (
    df.groupBy("drug_name")
      .agg(count("*").alias("review_count"))
      .orderBy(desc("review_count"))
      .limit(10)
)

pdf = most_reviewed.toPandas()

plt.figure(figsize=(10, 6))
plt.barh(pdf["drug_name"], pdf["review_count"])
plt.title("Top 10 Most Reviewed Drugs")
plt.xlabel("Review Count")
plt.ylabel("Drug Name")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("outputs/charts/most_reviewed_drugs.png")
plt.close()

# Chart 3: Average Rating by Effectiveness Category
effectiveness_rating = (
    df.groupBy("effectiveness")
      .agg(avg("rating").alias("avg_rating"))
      .orderBy(desc("avg_rating"))
)

pdf = effectiveness_rating.toPandas()

plt.figure(figsize=(9, 5))
plt.bar(pdf["effectiveness"], pdf["avg_rating"])
plt.title("Average Rating by Effectiveness Category")
plt.xlabel("Effectiveness Category")
plt.ylabel("Average Rating")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.savefig("outputs/charts/avg_rating_by_effectiveness.png")
plt.close()

spark.stop()