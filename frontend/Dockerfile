# Use Node.js 20 Alpine as base
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package files and install dependencies (cached)
COPY frontend/package*.json ./
RUN npm install

# Copy the rest of the source code
COPY frontend/ ./

# Expose the port
EXPOSE 3000

# Default command
CMD ["npm", "start"]
