FROM python:3.9
COPY requirements.txt ./requirements.txt
COPY app.py ./app.py
ENV MYSQL_HOST mysql_container
ENV MYSQL_USER root
ENV MYSQL_PASSWORD teste123456
ENV MYSQL_DATABASE flask
RUN pip install -r requirements.txt
CMD ["python", "./app.py"]
