# Reproduction Guide

This guide explains how to reproduce the project locally from raw data ingestion through final outputs.

## Requirements

Install the following software:

- Python 3.10+
- Apache Spark / PySpark
- Java 17
- Git

Verify installations:

```bash
python --version
spark-submit --version
java --version
```

## Clone the Repository

```bash
git clone <repository-url>
cd ITCS6190_SparkProject
```

## Dataset Setup

Download the Drug Review Dataset (Druglib.com) from the UCI Machine Learning Repository.

Place the raw dataset files in:

```text
local_data/
├── drugLibTrain_raw.tsv
└── drugLibTest_raw.tsv
```

The dataset is not included in the repository due to size constraints.

## Install Dependencies

Install required Python packages:

```bash
pip install -r requirements.txt
```

## Configure Java

The project was developed using Java 17.

On macOS:

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 17)
export PATH="$JAVA_HOME/bin:$PATH"
```

Verify:

```bash
java -version
```

## Run the Pipeline

Execute the full pipeline:

```bash
chmod +x run.sh
./run.sh
```

The pipeline performs:

1. Data ingestion
2. Data cleaning and transformation
3. Exploratory data analysis
4. MLlib classification
5. Output generation

## Generated Outputs

The project generates outputs in the following locations:

```text
outputs/
├── charts/
├── eda/
├── ml_metrics.txt
├── schema.txt
└── cleaned_schema.txt
```

Documentation is located in:

```text
docs/
```

Presentation slides are located in:

```text
docs/slides/
```

## Expected Results

The MLlib model should produce results similar to:

| Metric | Value |
|----------|----------|
| Accuracy | 88.31% |
| AUC | 0.938 |

Minor differences may occur depending on Spark and Java versions.

## Troubleshooting

### Java Version Errors

Verify Java 17 is active:

```bash
java -version
```

### Missing Dataset Errors

Confirm the following files exist:

```text
local_data/drugLibTrain_raw.tsv
local_data/drugLibTest_raw.tsv
```

### Spark Errors

Verify Spark is installed and available:

```bash
spark-submit --version
```

## Final Deliverables

The repository includes:

- Spark pipeline source code
- Documentation
- Visualizations
- MLlib evaluation metrics
- Final presentation slides

All project components can be reproduced using the steps described above.