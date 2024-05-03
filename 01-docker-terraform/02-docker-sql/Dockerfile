FROM python:3.9

RUN pip install pandas pyarrow

WORKDIR /app
COPY data-ingest.py data-ingest.py

ENTRYPOINT [ "python", "data-ingest.py" ]