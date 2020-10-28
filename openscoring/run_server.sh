java -jar bin/openscoring-server-executable-2.0.2.jar &
sleep 3 &
java -cp bin/openscoring-client-executable-2.0.2.jar org.openscoring.client.Deployer --model http://localhost:8080/openscoring/model/Titanic --file bin/titanic_clf.pmml 
