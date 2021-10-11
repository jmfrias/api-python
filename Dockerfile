FROM python:alpine3.14

RUN mkdir /apipython

WORKDIR /apipython

COPY requirements.txt .
ADD src src

RUN pip3 install -r requirements.txt
CMD ["python", "src/app.py"]