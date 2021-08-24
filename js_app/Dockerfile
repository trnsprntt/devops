FROM node:16-slim@sha256:5cf3448bd86f70498653613372b862564b3b8415e11a86c6ea229939bb3dba4a
WORKDIR /js_app
COPY package.json .
RUN npm install && npm cache clean --force
USER node
COPY --chown=node:node . .
EXPOSE 8000
ENTRYPOINT ["npm", "run", "dev"]

