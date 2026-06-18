# Results

## Exploratory Data Analysis Results

The EDA showed that medication satisfaction varies across drugs, conditions, effectiveness categories, and side-effect categories.

### Key Outputs

- Rating distribution
- Top and bottom drugs by average rating
- Average rating by medical condition
- Average rating by effectiveness category
- Average rating by side-effect category
- Review length comparison for positive and negative reviews

## Visualizations

The project includes the following visualizations:

- `outputs/charts/rating_distribution.png`
- `outputs/charts/most_reviewed_drugs.png`
- `outputs/charts/avg_rating_by_effectiveness.png`
- `outputs/charts/avg_rating_by_side_effects.png`

## Streaming Results

The Structured Streaming job simulates incoming medication review records from batch files. The stream updates average satisfaction metrics by drug using incoming records.

### Streaming Output

- Drug name
- Average rating
- Review count

The streaming pipeline demonstrates how Spark can process incoming review data and continuously update medication satisfaction metrics in near real time.

## MLlib Results

The MLlib classification model predicts whether a medication review reflects a positive or negative patient experience.

### Model

- Logistic Regression

### Features Used

- Effectiveness category
- Side-effect category
- Medical condition
- Review length

### Performance Metrics

| Metric | Value |
|----------|----------|
| Total Test Records | 710 |
| Correct Predictions | 627 |
| Accuracy | 88.31% |
| AUC | 0.938 |

### Interpretation

The model performed well at distinguishing positive and negative medication experiences. An accuracy of 88.31% indicates that most reviews were classified correctly, while an AUC of 0.938 demonstrates excellent discrimination between positive and negative outcomes.

These results suggest that effectiveness ratings, side-effect severity, medical condition, and review length are strong indicators of overall patient satisfaction.

Metrics are saved in:

```text
outputs/ml_metrics.txt
```

## Key Project Outcomes

- Successfully ingested and cleaned patient-reported medication review data using Apache Spark.
- Performed exploratory data analysis to identify medication satisfaction trends.
- Demonstrated Structured Streaming using simulated real-time review batches.
- Built and evaluated an MLlib Logistic Regression classifier.
- Achieved 88.31% classification accuracy and 0.938 AUC on the test dataset.
- Created a reproducible Spark pipeline integrating EDA, Streaming, and Machine Learning.