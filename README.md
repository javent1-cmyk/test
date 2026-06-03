# Patient-Reported Medication Experience Analytics Using Apache Spark

## Dataset Chosen

This project uses the Drug Review Dataset (Druglib.com) from the UCI Machine Learning Repository. The dataset contains patient-reported medication reviews, effectiveness ratings, side-effect ratings, satisfaction ratings, and medical conditions.

## Project Objective

The goal of this project is to build an Apache Spark pipeline that analyzes patient-reported medication experiences, performs exploratory data analysis, simulates real-time review ingestion, and develops a machine learning model to predict positive or negative medication experiences.

## How to Run Ingestion

Set Java 17:

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 17)
export PATH=$JAVA_HOME/bin:$PATH
```

Run the ingestion script:

```bash
spark-submit src/ingestion.py
```

## Initial Findings

Initial analysis showed that drug ratings vary significantly across medications and conditions. Visualizations were created to explore rating distributions, the most reviewed drugs, and average ratings by effectiveness category. These findings will support the streaming and MLlib components developed in later project milestones.
