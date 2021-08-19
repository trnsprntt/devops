ARG APP_IMAGE=python:3.6-alpine@sha256:a4b92be20bfbffa0f04fbbee596cbe66f012ad0c3a1e781a63a5d9b58e09f27f
FROM $APP_IMAGE AS base

FROM base as builder
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --prefix=/install -r /requirements.txt

FROM base
ENV FLASK_APP current_time_app.py
ENV FLASK_ENV development
WORKDIR /project
COPY --from=builder /install /usr/local
COPY . /project
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
