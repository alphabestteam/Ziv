# Dockerfile for app
FROM python

ENV DOCKERIZE_VERSION=v0.6.1

RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

COPY . ./app

WORKDIR ./app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4000

CMD ["dockerize", "-wait", "tcp://mysql:3306", "-timeout", "60s", "python", "app.py"]
