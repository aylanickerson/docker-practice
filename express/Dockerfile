FROM node
COPY package.json package.json
RUN npm install -g express
COPY ./app ./app
CMD ["node", "app/server.js"]