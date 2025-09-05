import json
import os

from google.cloud import bigquery
from google.oauth2 import service_account

DATA_FOLDER = "data"

keyfile = "KEYFILE_PATH"
service_account_info = json.load(open(keyfile))
credentials = service_account.Credentials.from_service_account_info(service_account_info)

project_id = "data-td-471107"       
dataset_id = "datasetq3"            

client = bigquery.Client.from_service_account_json(keyfile_path)


job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
)


def load_csv(table_name):
    file_path = f"{DATA_FOLDER}/{table_name}.csv"
    table_id = f"{project_id}.{dataset_id}.{table_name}"
    with open(file_path, "rb") as f:
        job = client.load_table_from_file(f, table_id, job_config=job_config)
    job.result()
    table = client.get_table(table_id)
    print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")


for t in ["sales_transaction", "product", "product_class"]:
    load_csv(t)
