# Dockerfile for frontend-dashboard
FROM node:20-alpine

WORKDIR /app

# Copy dependency files and install dependencies
COPY package.json package-lock.json ./
RUN npm ci

# Copy the rest of the source code
COPY . .

# Build the Next.js app
RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]