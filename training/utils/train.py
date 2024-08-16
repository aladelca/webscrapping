from utils.dataprep import data_prep
from xgboost import XGBRegressor    

def train_model(path):
    X, dataframe, vectorizer = data_prep(path)
    model = XGBRegressor(random_state=123)
    model.fit(X, dataframe['offer_price'])
    return model, vectorizer

