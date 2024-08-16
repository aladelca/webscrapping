from utils import train
from utils.save_files import save_model, load_file
import os
os.chdir('..')
path = 'bq_key.json'

def main():
    model, vectorizer = train.train_model(path)
    model_file = save_model(model)
    vector_file = save_model(vectorizer)
    load_file(model_file,'models/model.pkl')
    load_file(vector_file, 'models/vect.pkl')
    return model, vectorizer

if __name__ == '__main__':

    model, vectorizer = main()
    
    print('Model trained successfully')