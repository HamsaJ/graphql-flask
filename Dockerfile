FROM python:3.8

WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install -r requirements.txt
ENV FLASK_APP=app
ENV FLASK_ENV=development

CMD [ "flask", "run", "-h", "0.0.0.0" ]