from google.cloud import bigquery
from sklearn.feature_extraction.text import CountVectorizer
def get_data(path):
    
    # BigQuery client
    client = bigquery.Client.from_service_account_json(path)
    query = """
    SELECT *
    FROM `proyectodata-348005.precios.scrapped_data` 
    """
    dataframe = client.query(query).to_dataframe()
    return dataframe
def clean_title(text):
    text = text.lower()
    text = text.replace('"', '')
    return text

def prepare_data(dataframe):
    dataframe['title'] = dataframe['title'].apply(clean_title)
    dataframe = dataframe[~dataframe['offer_price'].isna()]
    return dataframe

def vectorize_data(dataframe):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(dataframe['title'])
    return X, vectorizer

def data_prep(path):
    dataframe = get_data(path)
    dataframe = prepare_data(dataframe)
    X, vectorizer = vectorize_data(dataframe)
    return X, dataframe, vectorizer