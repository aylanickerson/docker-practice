#using node base image
FROM node:latest 
#npm available bc of node base image 
#use npm to install serve to container globally with -g
RUN npm install -g serve
#copy takes a local dir as first arg and copies it into container dir as 2nd arg
COPY ./display ./display
#images need a default command to execute
CMD serve ./display
