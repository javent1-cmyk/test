from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
import os

# ---------------------------------------------------------
# 1. Start Spark session
# ---------------------------------------------------------
spark = SparkSession.builder \
    .appName("Drug Review MLlib Classification") \
    .getOrCreate()

# ---------------------------------------------------------
# 2. Load cleaned dataset
# ---------------------------------------------------------
df = spark.read.parquet("outputs/cleaned_drug_reviews.parquet")

print("Cleaned Dataset Schema:")
df.printSchema()

# ---------------------------------------------------------
# 3. Select columns for ML model
# Target variable: positive_review
# Features: effectiveness, sideEffects, condition_clean, review_length
# ---------------------------------------------------------
model_df = df.select(
    "effectiveness",
    "sideEffects",
    "condition_clean",
    "review_length",
    "positive_review"
).dropna()

# ---------------------------------------------------------
# 4. Split data into training and testing sets
# ---------------------------------------------------------
train_df, test_df = model_df.randomSplit([0.8, 0.2], seed=42)

# ---------------------------------------------------------
# 5. Convert categorical fields to numeric indexes
# ---------------------------------------------------------
effectiveness_indexer = StringIndexer(
    inputCol="effectiveness",
    outputCol="effectiveness_idx",
    handleInvalid="keep"
)

sideeffects_indexer = StringIndexer(
    inputCol="sideEffects",
    outputCol="sideeffects_idx",
    handleInvalid="keep"
)

condition_indexer = StringIndexer(
    inputCol="condition_clean",
    outputCol="condition_idx",
    handleInvalid="keep"
)

# ---------------------------------------------------------
# 6. Assemble all features into one feature vector
# ---------------------------------------------------------
assembler = VectorAssembler(
    inputCols=[
        "effectiveness_idx",
        "sideeffects_idx",
        "condition_idx",
        "review_length"
    ],
    outputCol="features"
)

# ---------------------------------------------------------
# 7. Define Logistic Regression model
# ---------------------------------------------------------
lr = LogisticRegression(
    labelCol="positive_review",
    featuresCol="features"
)

# ---------------------------------------------------------
# 8. Build ML pipeline
# ---------------------------------------------------------
pipeline = Pipeline(stages=[
    effectiveness_indexer,
    sideeffects_indexer,
    condition_indexer,
    assembler,
    lr
])

# ---------------------------------------------------------
# 9. Train model
# ---------------------------------------------------------
model = pipeline.fit(train_df)

# ---------------------------------------------------------
# 10. Generate predictions on test data
# ---------------------------------------------------------
predictions = model.transform(test_df)

print("Sample Predictions:")
predictions.select(
    "positive_review",
    "prediction",
    "probability"
).show(10, truncate=False)

# ---------------------------------------------------------
# 11. Evaluate model using AUC
# ---------------------------------------------------------
evaluator = BinaryClassificationEvaluator(
    labelCol="positive_review",
    rawPredictionCol="rawPrediction",
    metricName="areaUnderROC"
)

auc = evaluator.evaluate(predictions)

# ---------------------------------------------------------
# 12. Calculate accuracy
# ---------------------------------------------------------
correct_predictions = predictions.filter(
    predictions["positive_review"] == predictions["prediction"]
).count()

total_predictions = predictions.count()

accuracy = correct_predictions / total_predictions

# ---------------------------------------------------------
# 13. Save evaluation metrics
# ---------------------------------------------------------
os.makedirs("outputs", exist_ok=True)

with open("outputs/ml_metrics.txt", "w") as f:
    f.write("MLlib Classification Metrics\n")
    f.write("============================\n\n")
    f.write(f"Model: Logistic Regression\n")
    f.write(f"Target: positive_review\n")
    f.write(f"Features: effectiveness, sideEffects, condition_clean, review_length\n\n")
    f.write(f"Total test records: {total_predictions}\n")
    f.write(f"Correct predictions: {correct_predictions}\n")
    f.write(f"Accuracy: {accuracy:.4f}\n")
    f.write(f"AUC: {auc:.4f}\n")

print("MLlib Classification Metrics")
print("============================")
print(f"Accuracy: {accuracy:.4f}")
print(f"AUC: {auc:.4f}")
print("Metrics saved to outputs/ml_metrics.txt")

# ---------------------------------------------------------
# 14. Stop Spark session
# ---------------------------------------------------------
spark.stop()