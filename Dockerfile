FROM python:3.9

RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/*

RUN echo "es_ES.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen
RUN update-locale LANG=es_ES.UTF-8


WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./Movies_ETL.csv /code/
COPY ./functions.py /code/
COPY ./main.py /code/


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]