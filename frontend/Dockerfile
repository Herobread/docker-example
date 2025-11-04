FROM node:20-alpine

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# Run the dev server on port 3000
EXPOSE 3000
CMD ["npm", "start"]
