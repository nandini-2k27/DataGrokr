import pandas as pd


def extract(file_path):
    """Extract data from a CSV file."""
    return pd.read_csv(file_path)


def transform(df):
    """Clean and transform the dataset."""

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()

    # Fill missing values
    df["age"] = df["age"].fillna(df["age"].mean())
    df["salary"] = df["salary"].fillna(df["salary"].mean())

    # Calculate salary after 10% increment
    df["salary_after_increment"] = df["salary"] * 1.10

    return df


def load(df, output_path):
    """Load transformed data into a CSV file."""
    df.to_csv(output_path, index=False)


def run_pipeline(input_path, output_path):
    """Run the complete ETL pipeline."""

    print("Starting ETL Pipeline...")

    # Extract
    data = extract(input_path)
    print(f"Extracted {len(data)} rows.")

    # Transform
    transformed_data = transform(data)
    print(f"Transformed {len(transformed_data)} rows.")

    # Load
    load(transformed_data, output_path)
    print(f"Data successfully loaded into {output_path}")

    return transformed_data


if __name__ == "__main__":
    input_file = "input_data.csv"
    output_file = "output_data.csv"

    run_pipeline(input_file, output_file)