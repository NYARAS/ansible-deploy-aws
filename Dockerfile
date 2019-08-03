# FROM google/cloud-sdk:lates
FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
# RUN curl -sSL https://sdk.cloud.google.com | bash
# ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin
RUN pip install -r requirements.txt
ADD . /code/
CMD sh init.sh && python3 manage.py runserver 0.0.0.0:8000
