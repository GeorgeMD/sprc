FROM python:3.6

WORKDIR /app

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

COPY main.py /app
CMD python main.py