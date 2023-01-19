FROM node:16
WORKDIR /app
# COPY package.json ./
# COPY package-lock.json ./
# COPY ./public ./
# COPY ./src ./
COPY ./ ./
RUN npm i
CMD ["npm", "start"]