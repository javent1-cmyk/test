# Reproduction Guide

This guide explains how to run the project locally.

## Requirements

- Python
- Apache Spark / PySpark
- Java 17

## Dataset Setup

Download the Druglib dataset from the UCI Machine Learning Repository.

Place the full raw files in the local-only folder:

```text
local_data/
├── drugLibTrain_raw.tsv
└── drugLibTest_raw.tsv