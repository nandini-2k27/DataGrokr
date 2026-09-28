# ETL Pipeline with Unit Tests

A Python-based ETL (Extract, Transform, Load) pipeline that processes employee data stored in a CSV file. The project uses Pandas for data processing and Pytest for unit testing the ETL functions.

## Project Overview

The pipeline follows three main stages:

**Extract → Transform → Load**

- **Extract:** Reads employee data from a CSV file.
- **Transform:** Cleans the data, removes duplicate records, handles missing values, and calculates salary after a 10% increment.
- **Load:** Saves the transformed data into a new CSV file.

The project also includes unit tests to verify that each stage of the pipeline works correctly.

## Features

- Read data from CSV files
- Remove duplicate records
- Standardize column names
- Handle missing values
- Calculate salary after a 10% increment
- Save transformed data to a CSV file
- Analyze and validate the ETL process using unit tests
- Test file loading functionality

## Technologies Used

- Python 3
- Pandas
- Pytest
- CSV

## Project Structure

```text
Week 3(ETL Pipeline with Unit Tests)/
│
├── main.py
├── test_main.py
├── input_data.csv
├── output_data.csv
└── README.md
```

## ETL Workflow

```text
input_data.csv
      │
      ▼
   EXTRACT
      │
      ▼
   TRANSFORM
      │
      ├── Remove duplicates
      ├── Standardize column names
      ├── Handle missing values
      └── Calculate salary increment
      │
      ▼
     LOAD
      │
      ▼
output_data.csv
```

## Input Dataset

The input dataset contains employee information including:

- Name
- Age
- Department
- Salary

Example:

```text
Name,Age,Department,Salary
Nandini,22,IT,50000
Rahul,24,HR,45000
Priya,23,IT,60000
Aman,25,Finance,55000
```

## Transformation

During the transformation stage:

1. Duplicate records are removed.
2. Column names are converted to lowercase.
3. Missing age and salary values are replaced with the respective column mean.
4. A new column called `salary_after_increment` is created.
5. The new salary is calculated using a 10% increment.

Example:

```text
Salary = 50000
Salary after 10% increment = 55000
```

## Unit Testing

Pytest is used to test the ETL functions.

The project includes tests for:

- Data extraction
- Duplicate removal
- Salary increment calculation
- Loading transformed data

Run the tests using:

```bash
python -m pytest -v
```

### Test Result

All four tests pass successfully:

```text
test_main.py::test_extract PASSED
test_main.py::test_transform_removes_duplicates PASSED
test_main.py::test_transform_adds_salary_increment PASSED
test_main.py::test_load PASSED

4 passed
```

## How to Run

### 1. Install dependencies

```bash
python -m pip install pandas pytest
```

### 2. Run the ETL pipeline

```bash
python main.py
```

This generates:

```text
output_data.csv
```

### 3. Run unit tests

```bash
python -m pytest -v
```

## Learning Outcomes

This project provides practice with:

- ETL pipeline design
- Pandas DataFrames
- CSV data processing
- Data cleaning
- Data transformation
- File handling
- Functions
- Unit testing
- Pytest
- Test-driven validation

## Author

**Nandini Yadav**

This project was developed as part of the **DataGrokr Weekly Test - Week 3**.
