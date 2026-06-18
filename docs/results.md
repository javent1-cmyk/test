# Results

## Exploratory Data Analysis Results

The EDA showed that medication satisfaction varies across drugs, conditions, effectiveness categories, and side-effect categories.

Key outputs include:

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

Streaming output includes:

- Drug name
- Average rating
- Review count

## MLlib Results

The MLlib model predicts whether a medication review is positive or negative.

Model used:

- Logistic Regression

Features used:

- Effectiveness category
- Side-effect category
- Medical condition
- Review length

Metrics are saved in:

```text
outputs/ml_metrics.txt