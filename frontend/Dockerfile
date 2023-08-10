# Node.js Alpine image
FROM node:alpine

# Set the working directory
WORKDIR /app/frontend/blnk


COPY ./blnk /app/frontend/blnk

# Install dependencies
RUN npm install

# Expose the Vue.js port
EXPOSE 3000

CMD ["npm", "run", "serve"]
