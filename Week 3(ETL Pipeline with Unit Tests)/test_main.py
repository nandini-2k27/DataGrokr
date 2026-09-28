import pandas as pd
from main import extract, transform, load


def test_extract():
    df = extract("input_data.csv")

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 7


def test_transform_removes_duplicates():
    df = pd.DataFrame({
        "Name": ["A", "B", "A"],
        "Age": [20, 21, 20],
        "Department": ["IT", "HR", "IT"],
        "Salary": [40000, 50000, 40000]
    })

    transformed_df = transform(df)

    assert len(transformed_df) == 2


def test_transform_adds_salary_increment():
    df = pd.DataFrame({
        "Name": ["A"],
        "Age": [20],
        "Department": ["IT"],
        "Salary": [50000]
    })

    transformed_df = transform(df)

    assert "salary_after_increment" in transformed_df.columns
    assert round(transformed_df["salary_after_increment"].iloc[0], 2) == 55000

def test_load(tmp_path):
    df = pd.DataFrame({
        "name": ["A"],
        "age": [20],
        "department": ["IT"],
        "salary": [50000],
        "salary_after_increment": [55000]
    })

    output_file = tmp_path / "test_output.csv"

    load(df, output_file)

    loaded_df = pd.read_csv(output_file)

    assert len(loaded_df) == 1
    assert "name" in loaded_df.columns