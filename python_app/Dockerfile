FROM python:3.6-alpine@sha256:a4b92be20bfbffa0f04fbbee596cbe66f012ad0c3a1e781a63a5d9b58e09f27f

WORKDIR /python_app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

ENV FLASK_APP current_time_app
ENV FLASK_ENV development

RUN adduser -Ds /bin/bash -h /home/python_app flask 
USER flask
# WORKDIR /home/python_app
COPY --chown=flask:flask . .
EXPOSE 5000
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
