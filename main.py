from utils.loader import load_into_bq
from utils.scrapper import get_scrapped_data
from utils.utils import generate_dataframe
from google.oauth2 import service_account
import sys
import os
project_id = 'proyectodata-348005'
dataset_id = 'precios'
table_id = 'scrapped_data'


credentials = service_account.Credentials.from_service_account_file(
    'bq_key.json'
)

def main(text):
    titles, sellers, offer_prices, regular_prices, catalog_prices, brands, images = get_scrapped_data(text)
    df = generate_dataframe(titles, sellers, offer_prices, regular_prices, catalog_prices, brands, images)
    load_into_bq(project_id, dataset_id, table_id, df, credentials)
    return 'Data loaded successfully!'

if __name__ == '__main__':
    main(sys.argv[1])