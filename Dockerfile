FROM node:latest

COPY . /app

RUN cd app && npm install

WORKDIR /app

EXPOSE 3000

CMD ["node", "app.js"]