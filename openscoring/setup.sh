#!/bin/bash

# start openscoring server as background process
java -jar src/openscoring-server-executable-2.0.2.jar &

# wait sufficient amount of time for server to start
sleep 30

# load model as pmml
java -cp src/openscoring-client-executable-2.0.2.jar org.openscoring.client.Deployer --model http://localhost:8080/openscoring/model/Titanic --file src/titanic_clf.pmml

# keep running script - keeps docker image alive
sleep infinity