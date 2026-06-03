# Patient-Reported Medication Experience Analytics Using Apache Spark

## Dataset Chosen

This project uses the Drug Review Dataset (Druglib.com) from the UCI Machine Learning Repository. The dataset contains patient-reported medication reviews, effectiveness ratings, side-effect ratings, satisfaction ratings, review text, and medical conditions.

## Project Objective

The goal of this project is to build an Apache Spark pipeline that analyzes patient-reported medication experiences, performs exploratory data analysis (EDA), simulates real-time review ingestion, and develops a machine learning model to predict positive or negative medication experiences.

## How to Run

Set Java 17:

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 17)
export PATH=$JAVA_HOME/bin:$PATH
```

Run ingestion:

```bash
spark-submit src/ingestion.py
```

Run cleaning:

```bash
spark-submit src/cleaning.py
```

Run EDA:

```bash
spark-submit src/eda.py
```

Run visualizations:

```bash
spark-submit src/visualizations.py
```

## Initial Findings

Initial exploratory analysis found that:

- Satisfaction ratings vary across medications and medical conditions.
- Highly effective medications generally receive higher satisfaction ratings.
- Side-effect categories appear to influence overall satisfaction.
- The most reviewed drugs provide more reliable trends than drugs with few reviews.

Visualizations created:

- Rating Distribution
- Most Reviewed Drugs
- Average Rating by Effectiveness Category
- Average Rating by Side-Effects Category

These findings will support the Structured Streaming and MLlib components developed in later project milestones.
