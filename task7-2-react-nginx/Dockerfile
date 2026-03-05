# Build stage
FROM node:16-alpine AS build

WORKDIR /app
COPY package.json .
RUN npm install

COPY public/ ./public
COPY src/ ./src
RUN npm run build

# Production stage
FROM nginx:alpine

# Копируем собранные файлы из build stage
COPY --from=build /app/build /usr/share/nginx/html

# Копируем конфигурацию nginx
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
