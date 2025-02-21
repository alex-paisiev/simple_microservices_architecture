# Dockerfile for backend-service
FROM node:22-alpine

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy the source code
COPY . .

# Build the project
RUN npm run build

EXPOSE 4000

CMD ["node", "dist/main.js"]