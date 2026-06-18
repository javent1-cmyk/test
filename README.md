# ITCS6190 Spark Project

## Patient-Reported Medication Experience Analytics

This project analyzes patient-reported medication reviews using Apache Spark. The pipeline performs data ingestion, cleaning, exploratory data analysis (EDA), structured streaming, and MLlib classification to identify patterns in medication experiences and predict whether a review reflects a positive or negative patient outcome.

---

## Dataset

**Source:** UCI Drug Review Dataset (DrugLib)

**Files Used:**
- drugLibTrain_raw.tsv
- drugLibTest_raw.tsv

### Key Fields
- drug name
- condition
- rating
- effectiveness
- side effects
- review text

### Dataset Summary
- Training Reviews: ~161,000
- Test Reviews: ~54,000
- Total Reviews: ~215,000
- Original Features: 7

---

## Project Pipeline

```text
Ingestion → Cleaning → EDA → Streaming → MLlib → Results
```

### Data Ingestion
Raw TSV files are loaded into Spark DataFrames for scalable processing.

### Data Cleaning
Data preparation includes:
- Handling missing values
- Standardizing text fields
- Creating derived features
  - review_length
  - condition_clean
  - positive_review

### Exploratory Data Analysis (EDA)
EDA was performed using Spark DataFrames to analyze:
- Rating distributions
- Most reviewed medications
- Average ratings by effectiveness category
- Average ratings by side-effect category

### Structured Streaming
Structured Streaming simulates real-time patient review ingestion using micro-batches. Review events are processed and aggregated continuously to demonstrate streaming analytics.

### MLlib Classification
A Logistic Regression model was built using Spark MLlib to predict whether a review represents a positive or negative patient experience.

**Target Variable**
- positive_review
  - 1 = Positive Review
  - 0 = Negative Review

**Features**
- effectiveness
- sideEffects
- condition_clean
- review_length

---

## Model Results

| Metric | Value |
|----------|----------|
| Accuracy | 88.31% |
| AUC | 0.9380 |
| Test Records | 710 |
| Correct Predictions | 627 |

### Interpretation

The model successfully separates positive and negative patient experiences. An accuracy of 88.31% and AUC of 0.938 indicate strong predictive performance and excellent class discrimination.

---

## Repository Structure

```text
ITCS6190_SparkProject/
│
├── data/
├── docs/
│   ├── slides/
│   ├── dataset_overview.md
│   ├── methodology.md
│   ├── results.md
│   ├── limitations.md
│   └── reproduction_guide.md
│
├── local_data/
├── outputs/
│   ├── charts/
│   ├── eda/
│   ├── streaming/
│   ├── cleaned_schema.txt
│   ├── schema.txt
│   └── ml_metrics.txt
│
├── src/
│   ├── ingestion.py
│   ├── cleaning.py
│   ├── transformations.py
│   ├── eda.py
│   ├── visualizations.py
│   ├── create_stream_batches.py
│   ├── streaming.py
│   ├── ml_model.py
│   ├── dataset_summary.py
│   └── utils.py
│
├── run.sh
├── Makefile
├── requirements.txt
└── README.md
```

---

## Running the Project

### Set Java 17

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 17)
export PATH="$JAVA_HOME/bin:$PATH"
```

### Run Entire Pipeline

```bash
chmod +x run.sh
./run.sh
```

Or:

```bash
make run
```

---

## Key Outputs

Generated outputs include:

```text
outputs/charts/
outputs/eda/
outputs/streaming/
outputs/ml_metrics.txt
```

---

## Presentation

Final presentation slides:

```text
docs/slides/ITCS6190_SparkProject_FinalSlides.pptx
```

---

## Limitations

- Uses simulated streaming rather than a live production data source.
- Logistic Regression was selected as the primary classifier.
- Review text itself was not processed using advanced NLP techniques.

---

## Future Improvements

- Add NLP sentiment analysis
- Compare multiple MLlib models
- Integrate Kafka streaming
- Perform hyperparameter tuning
- Deploy to AWS