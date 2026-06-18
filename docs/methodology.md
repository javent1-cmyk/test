# Methodology

This project uses Apache Spark to build an end-to-end analytics pipeline for the Druglib medication review dataset.

## Pipeline Steps

1. **Data Ingestion**
   - Loaded the Druglib train and test TSV files using Spark DataFrames.
   - Combined both files into one dataset.

2. **Data Cleaning**
   - Removed duplicate records.
   - Dropped rows missing key fields.
   - Standardized drug and condition text.
   - Created derived fields:
     - `drug_name`
     - `condition_clean`
     - `review_length`
     - `positive_review`

3. **Exploratory Data Analysis**
   - Analyzed satisfaction ratings by drug and condition.
   - Examined rating distribution.
   - Compared average ratings by effectiveness and side-effect categories.

4. **Structured Streaming**
   - Simulated incoming medication reviews by splitting cleaned historical records into small batches.
   - Used Spark Structured Streaming to read incoming review batches.
   - Aggregated streaming records to update average satisfaction metrics by drug.

5. **MLlib Classification**
   - Trained a Logistic Regression classifier using Spark MLlib.
   - Target variable: `positive_review`
   - Features used:
     - `effectiveness`
     - `sideEffects`
     - `condition_clean`
     - `review_length`
   - Evaluated the model using accuracy and AUC.