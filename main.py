import pandas as pd
import os
import boto3
import logging

df = pd.read_csv('walmart_sales.csv')
df_sorted_store = df.sort_values(by='Weekly_Sales', ascending=False)
#print(df_sorted_store.head(50))
df_drop = df.dropna()

df_types = df_drop.columns


df_sort = df_drop.sort_values(by=['Weekly_Sales', 'Store'], ascending=[False, True])
df_dropped = df_drop.drop(columns=['Holiday_Flag', 'CPI', 'Unemployment'])
df_drop_dup = df_dropped.drop_duplicates()


with open('walmart_sales_cleaned.csv', 'w') as f:
    df_drop_dup.to_csv(f, index=False)



file_name = 'walmart_sales_cleaned.csv'

def upload_file(file_name, bucket, object_name=None, extra_args=None):
    if object_name is None:
        object_name = os.path.basename(file_name)
    s3_client = boto3.client('s3')
    try:
        if extra_args:
            s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=extra_args)
        else:
            s3_client.upload_file(file_name, bucket, object_name)

    except Exception as e:
        logging.error('S3 upload failed: %s', e)
        return False
    return True 

result = upload_file(file_name, 'mybricks34', 'walmart_sales_cleaned.csv', extra_args={'Metadata': {'mykey' : 'myvalue'}})
if result:
    print("Upload Successful")
else:
    print("Upload Failed")