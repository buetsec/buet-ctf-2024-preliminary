# Use the official Node.js image from the Docker Hub
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install the necessary dependencies
RUN npm install

# Copy the rest of your application code
COPY . .

# Expose the port your app runs on (update this if your app runs on a different port)
EXPOSE 3000

# Command to run your app
CMD ["npm", "run", "start"]
