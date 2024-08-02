## data_cleaning.py
import pandas as pd

def clean_data(file_path):
    # Load the data
    df = pd.read_csv(file_path)

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Handle missing values (example: fill NaN with mean of the column)
    # Select only numeric columns for mean calculation
    numeric_cols = df.select_dtypes(include=['float', 'int']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # Convert 'Order Date' and 'Ship Date' to datetime
    # Check if the column names exist before conversion
    if 'Order Date' in df.columns:
        df['Order Date'] = pd.to_datetime(df['Order Date'])
    else:
        print("Warning: 'Order Date' column not found.")

    if 'Ship Date' in df.columns:
        df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    else:
        print("Warning: 'Ship Date' column not found.")

    return df

if __name__ == "__main__":
    file_path = '/content/Sample_Superstore.csv'
    cleaned_data = clean_data(file_path)
    cleaned_data.to_csv('/content/Sample_Superstore.csv', index=False)

## eda.py

import pandas as pd

def perform_eda(df):
    # Basic statistics
    print(df.describe())

    # Check for missing values
    print(df.isnull().sum())

    # Distribution of 'Sales'
    print(df['Sales'].describe())

    # Correlation matrix (only for numeric columns)
    print(df.select_dtypes(include=['float', 'int']).corr()) # Select numeric columns

    # Group by 'Category' and 'Sub-Category' to see sales and profit
    category_sales = df.groupby(['Category', 'Sub-Category'])[['Sales', 'Profit']].sum()
    print(category_sales)

    return category_sales

if __name__ == "__main__":
    file_path = '/Sample_Superstore.csv'
    df = pd.read_csv(file_path)
    category_sales = perform_eda(df)
    category_sales.to_csv('/Sample_Superstore.csv')
    
## visualizations.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def create_visualizations(df):
    # Create the 'visualizations' directory if it doesn't exist
    if not os.path.exists('visualizations'):
        os.makedirs('visualizations')

    # Sales distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Sales'], bins=50, kde=True)
    plt.title('Sales Distribution')
    plt.xlabel('Sales') # Removed extra indent here
    plt.ylabel('Frequency') # Removed extra indent here
    plt.savefig('visualizations/sales_')
    
## main.py

import pandas as pd
from scripts.data_cleaning import clean_data
from scripts.eda import perform_eda
from scripts.visualizations import create_visualizations

def main():
    # Step 1: Clean the data
    file_path = '/Sample_Superstore.csv'
    cleaned_data = clean_data(file_path)
    cleaned_data.to_csv('path/to/save/cleaned_data.csv', index=False)
    
    # Step 2: Perform EDA
    category_sales = perform_eda(cleaned_data)
    category_sales.to_csv('path/to/save/category_sales.csv')
    
    # Step 3: Create Visualizations
    create_visualizations(cleaned_data)

if __name__ == "__main__":
    main()


