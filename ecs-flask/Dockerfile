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
    && conda env create -n ecsdemo -f environment.yml \
    && rm -rf /opt/conda/pkgs/* 
ENV PATH /opt/conda/envs/ecsdemo/bin:$PATH

# expose on port 8080
EXPOSE 80

# activate conda environment
CMD ["bash", "conda activate ecsdemo"]

# coppy server and startup script
COPY src src
COPY start.sh start.sh

# copy model binary
COPY bin/market-invoice-lgb.pkl bin/market-invoice-lgb.pkl

# start gunicorn - todo, configure with Nginx
#CMD ["bash" ,"start.sh"]

CMD [ "python3", "src/server/main.py" ]

