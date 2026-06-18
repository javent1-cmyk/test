# Limitations

This project has several limitations.

## Dataset Limitations

The dataset is based on patient-reported medication reviews. These reviews may include personal bias, incomplete information, or inconsistent reporting.

Some drugs and conditions have fewer reviews than others, which can make average ratings less reliable for small groups.

## Streaming Limitations

The streaming pipeline uses simulated incoming data created from historical records. It does not connect to a live data source.

The streaming job demonstrates Spark Structured Streaming functionality, but it is not designed for production-level throughput or real-time healthcare monitoring.

## Model Limitations

The MLlib model uses a basic Logistic Regression classifier. It uses a limited set of structured features and does not deeply analyze review text.

The model results should be interpreted as a demonstration of Spark MLlib classification, not as a clinical or medical prediction tool.

## Project Scope Limitations

This project is intended for educational purposes and focuses on demonstrating Spark Structured APIs, Structured Streaming, and MLlib in one pipeline.