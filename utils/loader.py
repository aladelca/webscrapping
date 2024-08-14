import pandas as pd
from pandas_gbq import to_gbq
from google.oauth2 import service_account
import os


def load_into_bq(project_id, dataset_id, table_id, data, credentials):
    print('Data to be inserted:',data.shape)
    table_full_name = f'{project_id}.{dataset_id}.{table_id}'
    to_gbq(data, table_full_name, project_id=project_id, if_exists='append', credentials=credentials)
    
    return f'Table {table_full_name} loaded successfully!'


