import pandas as pd


def main():
    df = pd.read_csv("csv_files/Sales.csv")
    print(df)
    print(f"\nDataFrame shape: {df.shape}")
    print(f"Column names: {list(df.columns)}")


if __name__ == "__main__":
    main()
