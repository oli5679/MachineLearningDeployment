# Serverless Python with Zappa

This template demonstrates how to make a simple REST API with Python running on AWS Lambda and API Gateway using 'Zappa'

https://github.com/Miserlou/Zappa

Based on this guide https://towardsdatascience.com/how-to-deploy-a-machine-learning-model-on-aws-lambda-24c36dcaed20

## Prerequesites

AWS account

Create the model artefact (see 'fit-model') and copy over to .bin

## Create and activate virtual-env

    pip install virtualenv
    virtualenv zappa_test
    source your_virtual_environment_name/bin/activate
    pip install -r requirements.txt

## Run Flask app

    export FLASK_APP=server.py
    flask run

## Test flask App

    curl --location --request POST 'http://127.0.0.1:5000/' \
    --header 'Content-Type: application/json' \
    --data-raw '{"input": [{"Male": 0, "Age": 21, "SibSp": 0, "Parch": 0, "Fare": 21.5}]}'

## Deploy to AWS

    environment --> dev
    "app_function --> server.app

    zappa init

Change zappa_settings.json to --> "slim_handler": true

    zappa deploy your-environment-name

The same curl command will test, but with the deployed app url