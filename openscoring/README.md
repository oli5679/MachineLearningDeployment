# Openscoring

Tool for inference from machine learning models compiled as 'PMML' artefacts.

## Dependencies

Get binaries from here https://github.com/openscoring/openscoring

    brew cask install java

## Start openscoring server

    java -jar bin/openscoring-server-executable-2.0.2.jar

## Build and run docker image

    sudo docker run --net="host" jpmml/openscoring:latest



## Upload model

    java -cp bin/openscoring-client-executable-2.0.2.jar org.openscoring.client.Deployer --model http://localhost:8080/openscoring/model/Titanic --file bin/titanic_clf.pmml

## Endpoints

    - HTTP method	Endpoint	Required role(s)	Description
    - GET	/model	-	Get the summaries of all models
    - PUT	/model/${id}	admin	Deploy a model
    - GET	/model/${id}	-	Get the summary of a model
    - GET	/model/${id}/pmml	admin	Download a model as a PMML document
    - POST	/model/${id}	-	Evaluate data in "single prediction" mode
    - POST	/model/${id}/batch	-	Evaluate data in "batch prediction" mode
    - POST	/model/${id}/csv	-	Evaluate data in "CSV prediction" mode
    - DELETE	/model/${id}	admin	Undeploy a model

## Test endpoint

    curl --location --request POST 'http://localhost:8080/openscoring/model/Titanic' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "id" : "record-001",
        "arguments" : {
            "x1" : 5.1,
            "x2" : 3.5,
            "x3" : 1.4,
            "x4" : 0.2
        }
    }'
