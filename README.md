# walmartsales-pipeline
ETL pipeline that cleans and transforms Walmart Sales data and stores in AWS S# bucket

🛒 Walmart Sales ETL Pipeline

Python • Pandas • Boto3 • Logging • AWS S3

This repository contains an ETL (Extract, Transform, Load) pipeline that processes Walmart sales data from a CSV file, cleans and transforms the dataset using Pandas, logs every step of the process using Python’s logging module, and uploads the final cleaned file to an AWS S3 bucket using Boto3.

📌 Features

Extraction

Reads raw Walmart sales CSV files.

Logs start/end of extraction and file validation.

Transformation

Cleans missing or inconsistent values.

Converts date and numeric columns.

Creates new calculated fields like revenue.

Logs each transformation step for transparency.

Loading

Exports cleaned dataset to JSON or CSV.

Uploads processed file to AWS S3 using Boto3.

Logs upload status and success/failure messages.

🗂️ Project Structure
.
├── data/
│   └── walmart_sales_raw.csv
├── etl_pipeline.py
├── requirements.txt
└── README.md

⚙️ Technologies Used

Python 3.x

Pandas – data cleaning and transformation

Boto3 – AWS S3 integration

Logging – detailed ETL run logs

AWS S3 – cloud storage destination

🚀 How to Run the Pipeline
1. Install Dependencies
pip install -r requirements.txt

2. Configure AWS Credentials

Use one of these methods:

aws configure

Environment variables

.aws/credentials file

IAM user must have PutObject permissions on your S3 bucket.

3. Run the ETL Script
python etl_pipeline.py


Logs will generate in the terminal or in your specified .log file.

🧼 Example Transformation Steps

Remove duplicates

Convert “Date” column to datetime

Ensure numeric columns (units sold, prices) are correctly typed

Compute revenue column

Standardize formatting of strings and categories

☁️ AWS S3 Upload

The pipeline uses boto3.client("s3") to upload:

s3.upload_file(
    "cleaned_walmart_sales.json",
    "your-s3-bucket",
    "walmart/cleaned_walmart_sales.json"
)

📝 Example etl_pipeline.py Outline
import pandas as pd
import boto3
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def extract(file_path):
    logging.info("Starting data extraction...")
    df = pd.read_csv(file_path)
    logging.info(f"Extracted {len(df)} rows.")
    return df

def transform(df):
    logging.info("Starting data transformation...")

    df.drop_duplicates(inplace=True)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]

    logging.info("Transformation complete.")
    return df

def load(df, bucket, key):
    output_file = "cleaned_walmart_sales.json"
    df.to_json(output_file, orient="records")

    logging.info(f"Uploading {output_file} to S3...")
    s3 = boto3.client("s3")
    s3.upload_file(output_file, bucket, key)
    logging.info("Upload successful!")

if __name__ == "__main__":
    raw_df = extract("data/walmart_sales_raw.csv")
    clean_df = transform(raw_df)
    load(clean_df, "your-s3-bucket", "walmart/cleaned_walmart_sales.json")

📈 Ideal Use Cases

Data engineering portfolio project

Learning ETL workflows with Python

Practicing S3 and cloud storage integration

Automating retail data cleanup tasks
