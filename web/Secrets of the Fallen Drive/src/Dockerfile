FROM --platform=linux/amd64 node:18

# Copy package files
WORKDIR app
COPY . ./

# Install dependencies
RUN npm ci

RUN npm run build --if-present

# Expose port and run server
EXPOSE 3000
CMD ["npm", "start"]
