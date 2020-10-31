# Fastapi demo

Example of deploying machine learning model API on AWS using docker & fastapi

Work in progress

## prerequestites

Docker - https://docs.docker.com/docker-for-mac/install/

AWS - https://aws.amazon.com/

AWS cli - https://docs.aws.amazon.com/polly/latest/dg/setup-aws-cli.html


## run outside of Docker

    conda env create -n fastapidemo -f environment.yml
    conda activate fastapidemo
    uvicorn main:app --host 0.0.0.0 --port 80

go to http://0.0.0.0:80/docs for API docs and chance to test locally

## run tests

    pytest .

## rebuild and run docker image locally

build a livescoring API as docker image (flask+nginx+conda)

    docker build -t fastapidemo .
    docker run  -p 80:80 fastapidemo

## push to ECR

setup AWS cli, look up account id and then run the following commands

    aws ecr create-repository --repository-name fastapi-demo

    aws ecr get-login --region eu-west-2 --no-include-email

[run the login snippet]

[replace with actual account id]

    docker tag fastapi-demo:latest [account_id].dkr.ecr.eu-west-2.amazonaws.com/fastapi-demo

    docker push [account_id].dkr.ecr.eu-west-2.amazonaws.com/fastapi-demo

TODO - investigate proper CI/CD pipeline

## deploy app on ECS

TODO add details
