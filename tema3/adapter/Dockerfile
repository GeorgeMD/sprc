FROM python:3.6

WORKDIR /adapter

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

COPY adapter.py /adapter
CMD ["python", "-u", "adapter.py"]
