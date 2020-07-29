FROM continuumio/miniconda:latest

# Set the working directory to /app
WORKDIR /opt/app

RUN apt-get update && apt-get clean

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY ./ .

RUN conda create python=3.7 --name sample_logreg --file requirements.txt
RUN echo "source activate sample_logreg" > ~/.bashrc
ENV PATH /opt/conda/envs/sample_logreg/bin:$PATH

# to avoid ModuleNotFoundError: No module named 'api'
ENV PYTHONPATH="$PYTHONPATH:/"

EXPOSE 8000
ENTRYPOINT ["python3", "api.py"]