# ECS demo

Example of deploying machine learning model API on AWS using docker+conda+flask+nginx+gunicorn

Based on this resource:

https://linuxacademy.com/blog/linux-academy/deploying-a-containerized-flask-application-with-aws-ecs-and-docker/

Work in progress

## prerequestites

Conda - https://docs.conda.io/projects/conda/en/latest/user-guide/install/

Docker - https://docs.docker.com/docker-for-mac/install/

AWS - https://aws.amazon.com/

AWS cli - https://docs.aws.amazon.com/polly/latest/dg/setup-aws-cli.html

## rebuild model

Fits classifier based on bin/market-invoice-data.csv & saves model binary as .pkl file

    conda config --add channels conda-forge 
    conda env create -n ecsdemo -f environment.yml 
    conda activate ecsdemo
    python3 src/model/fit_model.py

TODO - add custom sklearn transformer to demo


## rebuild and run docker image locally

build a livescoring API as docker image (flask+nginx+conda)

    docker build -t oli5679/ecsdemo .
    docker run  -p 80:80 oli5679/ecsdemo

Also fits 'Shap' explainer, that can explain feature impacts on model prediction.

TODO - get gunicorn working on ecs

TODO - add NGINX

## test local api
post to localhost:80/score to test live scoring

TODO add more details


## push to ECR
setup AWS cli, look up account id and then run the following commands

    aws ecr create-repository --repository-name flask-ecs-demo

    aws ecr get-login --region eu-west-2 --no-include-email

[run the login snippet]

[replace with actual account id]

    docker tag oli5679/ecsdemo:latest 782247268784.dkr.ecr.eu-west-2.amazonaws.com/flask-ecs-demo

    docker push 782247268784.dkr.ecr.eu-west-2.amazonaws.com/flask-ecs-demo

TODO - investigate adding unit tests + Jenkins build pipeline 

## deploy app on ECS

follow step 4 and onwards from here https://linuxacademy.com/blog/linux-academy/deploying-a-containerized-flask-application-with-aws-ecs-and-docker/


TODO - investigate automating with teraform/jenkins, and also increasign security/IAM

TODO - investigate autoscaling and logging

TODO - investigate eks

## test app 

lookup url on ECS console, and post to url + /score

TODO add more details

## Other links

https://www.bogotobogo.com/DevOps/Docker/Docker-Flask-ALB-ECS.php

https://towardsdatascience.com/how-to-do-rapid-prototyping-with-flask-uwsgi-nginx-and-docker-on-openshift-f0ef144033cb

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-14-04

https://aws.amazon.com/blogs/devops/set-up-a-build-pipeline-with-jenkins-and-amazon-ecs/
