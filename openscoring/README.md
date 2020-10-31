## Openscoring demo

Creates rest API for machine learning model(s) specified as PMML documents

API details https://github.com/openscoring/openscoring

### Setup

Install and run docker https://www.docker.com/

Export model as PMML https://cran.r-project.org/web/packages/pmml/index.html

add PMML to src directory (for now using Thor model), and change setup.sh command to reference PMML and desired model name

### Deploy

    # only need to do this if code has changed
    docker build -t openscoring_demo .

    # make sure nothing else is running on port 1234, or change port in docker run command, and Dockerfile expose
    docker run -p 1234:8080 openscoring_demo

