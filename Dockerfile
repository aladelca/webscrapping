FROM public.ecr.aws/lambda/python:3.12


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV AWS_DEFAULT_REGION=us-east-1

COPY predict/. .

CMD ["main_predict.lambda_handler"]
