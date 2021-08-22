FROM python:3.6-alpine@sha256:a4b92be20bfbffa0f04fbbee596cbe66f012ad0c3a1e781a63a5d9b58e09f27f

WORKDIR /python_app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

ENV FLASK_APP current_time_app.py
ENV FLASK_ENV development

COPY . .
RUN addgroup -g 1000 flask && adduser -HDs /bin/bash flask -u 1000 -G flask
USER flask
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
