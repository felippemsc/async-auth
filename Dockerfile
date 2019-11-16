FROM python:3.8-alpine

EXPOSE 8000

COPY . app
WORKDIR app

RUN apk add --no-cache postgresql-dev gcc python3-dev binutils libc-dev

RUN pip install --no-cache-dir -U pip pipenv
RUN pipenv install --system

CMD gunicorn -w 4 -b 0.0.0.0:8000 -k aiohttp.worker.GunicornWebWorker main:app