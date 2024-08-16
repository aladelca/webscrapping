import boto3
import os
import pickle
import io


def save_model(model):
    pickle_buffer = io.BytesIO()
    pickle.dump(model, pickle_buffer)
    pickle_buffer.seek(0)
    return pickle_buffer

def load_file(object,model_file_key):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=str(os.environ['AWS_ACCESS_KEY_ID']),
        aws_secret_access_key=os.environ['AWS_SECRET_KEY'],
        region_name='us-east-1'  
    )

    bucket_name = 'scrapping-exercise'
    #model_file_key = 'models/model.pkl'

    s3_client.upload_fileobj(object, bucket_name, model_file_key)
    

    