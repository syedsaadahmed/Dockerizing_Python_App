FROM python:alpine3.7
MAINTAINER Syed Saad Ahmed, syedsaadahmed2094.sa@gmail.com
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./index.py