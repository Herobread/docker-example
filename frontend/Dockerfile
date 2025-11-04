# Use an official Node.js runtime as a parent image.
# Using a specific version is recommended for production.
FROM node:20-alpine

# Set the working directory in the container.
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock) to leverage Docker cache.
COPY package*.json ./

# Install project dependencies.
RUN npm install

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . .

# Make port 3000 available to the world outside this container.
EXPOSE 3000

# The command to run when the container starts.
CMD ["npm", "start"]