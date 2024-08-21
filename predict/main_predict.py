from utils.predict import predict
import sys
import warnings
warnings.filterwarnings("ignore")



def main_predict(text):

    model_path = 'model.pkl'
    vect_path = 'vect.pkl'
    
    return predict(model_path, vect_path, text)

def lambda_handler(event, context):
    print(event)
    return 'Hello from Lambda!'

#print(main_predict(sys.argv[1]))