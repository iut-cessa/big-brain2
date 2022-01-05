FROM dockerhub.ir/python:3.10
WORKDIR "/BigBrain"
COPY requirements.txt ./requirements.txt
COPY uwsgi.ini ./uwsgi.ini
RUN pip3 install uwsgi
RUN pip3 install -r requirements.txt
RUN pip3 install psycopg2-binary==2.8.5
#RUN pip3 install psycopg2==2.7.5
RUN mkdir src
COPY ./BigBrain/ ./src/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR "/BigBrain/src"
CMD python manage.py migrate;python manage.py collectstatic ; uwsgi --ini /BigBrain/uwsgi.ini
