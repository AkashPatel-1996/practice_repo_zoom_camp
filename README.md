## 01 Intro

Here are all the things mentioned in Homework module is present.




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

![Screenshot 2024-06-30 191531](https://github.com/AkashPatel-1996/practice_repo_zoom_camp/assets/84029971/6de1579f-2f12-41ee-a4aa-f72df6ff0211)

# best Practices
Clear Repository Structure:

Organize your repository with clear directories for code, data, models, and documentation.
Include a detailed README.md file explaining the project's purpose, setup instructions, and usage guidelines.
Version Control with Git:

Use Git for version control to track changes and collaborate effectively.
Commit regularly with descriptive messages to document changes and improvements.
Modular and Documented Code:

Write modular code with functions or classes for preprocessing, model training, and evaluation.
Include comments and docstrings to explain the purpose of functions, parameters, and data transformations.
Testing and Validation:

Implement unit tests and integration tests to validate each component of your machine learning pipeline.
Use continuous integration (CI) tools like GitHub Actions to automate testing and ensure code quality.
Documentation and Collaboration:

Document your model development process, including data preprocessing, model training, and evaluation metrics.
Encourage collaboration by providing clear guidelines for contributions, code reviews, and issue tracking.



# Deployment

![deployment_screenshot](https://github.com/AkashPatel-1996/practice_repo_zoom_camp/assets/84029971/5b9af56a-554c-41f1-945a-169031e047c1)


