
## `docs/dataset_overview.md`

```markdown
# Dataset Overview

## Dataset

This project uses the Drug Review Dataset (Druglib.com) from the UCI Machine Learning Repository.

Dataset URL: https://archive.ics.uci.edu/dataset/461/drug+review+dataset+druglib.com

## Description

The dataset contains patient-reported medication reviews. Each review includes information about the medication, condition, effectiveness, side effects, overall satisfaction rating, and written review text.

## Files Used

The original dataset includes:

- `drugLibTrain_raw.tsv`
- `drugLibTest_raw.tsv`

The full raw files are stored locally in `local_data/` and are not committed to GitHub. Small sample files are stored in `data/sample/`.

## Main Fields

Important fields include:

- `urlDrugName`: medication name
- `condition`: medical condition
- `rating`: overall satisfaction rating
- `effectiveness`: patient-reported effectiveness category
- `sideEffects`: patient-reported side effects category
- `benefitsReview`: review text about benefits
- `sideEffectsReview`: review text about side effects
- `commentsReview`: general review comments

## Preprocessing

The Week 3 cleaning step included:

- Combining train and test datasets
- Removing duplicate records
- Dropping rows missing key fields
- Standardizing drug and condition text
- Creating `drug_name`
- Creating `condition_clean`
- Creating `review_length`
- Creating `positive_review`

## Use in Project

This dataset will be used for:

- Exploratory analysis of medication satisfaction patterns
- Simulated streaming ingestion of new medication reviews
- MLlib classification to predict positive or negative patient experiences