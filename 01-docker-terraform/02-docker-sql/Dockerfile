FROM python:3.9

RUN pip install pandas pyarrow argparse sqlalchemy psycopg2-binary

WORKDIR /app
COPY data-ingest.py data-ingest.py

ENTRYPOINT [ "python", "data-ingest.py" ]