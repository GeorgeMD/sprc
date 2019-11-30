FROM python:3.6

EXPOSE 8080

WORKDIR /app

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

COPY app.py /app
CMD ["python", "app.py"]