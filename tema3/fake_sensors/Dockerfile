FROM python:3.6

WORKDIR /fake_sensors

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

COPY fake_sensors.py /fake_sensors
CMD ["python", "-u", "fake_sensors.py"]