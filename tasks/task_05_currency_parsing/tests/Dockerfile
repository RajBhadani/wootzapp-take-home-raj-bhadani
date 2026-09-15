FROM python:3.11-slim

WORKDIR /tests

COPY hidden_data /tests/hidden_data
COPY grader.py /tests/grader.py
COPY test.sh /tests/test.sh

RUN pip install --no-cache-dir pandas && chmod +x /tests/test.sh