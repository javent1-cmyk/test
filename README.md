## Project Pipeline

```text
Ingestion → Cleaning → EDA → Structured Streaming → MLlib Classification → Results
```

### Data Ingestion

Raw DrugLib TSV files are loaded into Spark DataFrames for distributed processing.

### Data Cleaning

Data preparation includes:

* Handling missing values
* Standardizing text fields
* Creating derived features:

  * `review_length`
  * `condition_clean`
  * `positive_review`

### Exploratory Data Analysis (EDA)

EDA was performed using Spark DataFrames to analyze:

* Rating distributions
* Most reviewed medications
* Average ratings by effectiveness category
* Average ratings by side-effect category
* Condition-level medication performance

### Structured Streaming

Structured Streaming demonstrates real-time processing using simulated micro-batches generated from historical review data.

Streaming outputs include:

* Drug name
* Average rating
* Review count

Streaming files are written to:

```text
outputs/streaming/
```

### MLlib Classification

A Logistic Regression model was built using Spark MLlib to predict whether a review represents a positive or negative patient experience.

#### Target Variable

* `positive_review`

  * `1 = Positive Review`
  * `0 = Negative Review`

#### Features

* effectiveness
* sideEffects
* condition_clean
* review_length

---

## Running the Project

### Set Java 17

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 17)
export PATH="$JAVA_HOME/bin:$PATH"
```

### Run Core Pipeline

```bash
chmod +x run.sh
./run.sh
```

The core pipeline executes:

* Data ingestion
* Feature transformation
* MLlib classification

### Run Structured Streaming Demo

Generate streaming batches:

```bash
python src/create_stream_batches.py
```

Start the streaming application:

```bash
python src/streaming.py
```

This demonstrates Spark Structured Streaming using simulated incoming medication review records.

---

## Key Outputs

Generated outputs include:

```text
outputs/charts/
outputs/eda/
outputs/streaming/
outputs/ml_metrics.txt
```
