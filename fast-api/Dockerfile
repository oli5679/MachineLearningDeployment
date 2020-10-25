FROM continuumio/miniconda3

# clean up impage
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Do not run as root
RUN groupadd -r myuser && useradd -r -g myuser myuser
WORKDIR /app

# Install conda environment and add to path
COPY environment.yml /app/environment.yml
RUN conda config --add channels conda-forge \
    && conda env create -n fastapidemo -f environment.yml \
    && rm -rf /opt/conda/pkgs/* 
ENV PATH /opt/conda/envs/fastapidemo/bin:$PATH

# expose on port 8000
EXPOSE 80

# copy model binary
COPY bin/ bin/
COPY main.py main.py 

CMD ["conda", "activate","fastapidemo"]


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]