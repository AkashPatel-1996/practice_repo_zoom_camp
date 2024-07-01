
## 02) Experiment Tracking

This Python script prepares NYC taxi trip data for machine learning tasks. It reads raw data from Parquet files, performs preprocessing including feature engineering and categorical encoding using `DictVectorizer` from scikit-learn, and then saves the preprocessed data and model artifacts.

## Features

- Reads raw NYC taxi trip data in Parquet format.
- Computes the trip duration in minutes and filters trips with durations between 1 and 60 minutes.
- Converts categorical features (`PULocationID` and `DOLocationID`) to strings.
- Uses `DictVectorizer` to encode categorical features and numerical features (`trip_distance`) into a sparse matrix.
- Saves the preprocessed datasets (`train.pkl`, `val.pkl`, `test.pkl`) and the fitted `DictVectorizer` (`dv.pkl`) to a specified destination folder.

## Usage

### Prerequisites

- Python 3.x
- Pandas
- Scikit-learn
- Click

### ML Flow

Use ml flow to do experiment tracking using various paramters.

![ML_Flow_screenshot2](https://github.com/AkashPatel-1996/practice_repo_zoom_camp/assets/84029971/0c787abb-8fe3-48b7-b4f4-39fa14094e50)


# Orchestration

![ML_Flow_screenshot2](https://github.com/AkashPatel-1996/practice_repo_zoom_camp/assets/84029971/5ae4b75f-7a19-49e3-8a0b-6901f73c79c2)

