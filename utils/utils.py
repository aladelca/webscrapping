import pandas as pd
import numpy as np

def prepare_name(text):
    text = text.replace(' ', '+')
    text = text.lower()
    return text

def filter_nan(df):
    return df[df['title'].notna()]

def clean_prices(price):
    try:
        return float(price.replace('S/','').replace(',','').replace('.',''))
    except:
        return np.nan

def generate_dataframe(titles, sellers, offer_prices, regular_prices, catalog_prices, brands, images):
    data = pd.DataFrame()
    data['title'] = titles
    data['seller'] = sellers
    data['offer_price'] = offer_prices
    data['regular_price'] = regular_prices
    data['catalog_price'] = catalog_prices
    data['brand'] = brands
    data['image'] = images
    print('Before filter:',data.shape)
    data = filter_nan(data)
    print('After filter:',data.shape)
    
    data['offer_price'] = data['offer_price'].apply(clean_prices)
    data['regular_price'] = data['regular_price'].apply(clean_prices)
    data['catalog_price'] = data['catalog_price'].apply(clean_prices)
    return data

