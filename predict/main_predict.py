from utils.predict import predict
import sys
import warnings
import json
warnings.filterwarnings("ignore")



def main_predict(text):

    model_path = 'model.pkl'
    vect_path = 'vect.pkl'
    
    return predict(model_path, vect_path, text)

def lambda_handler(event, context):
    data = json.loads(json.dumps(event))
    text = data['text']
    return main_predict(text)

#print(main_predict(sys.argv[1]))