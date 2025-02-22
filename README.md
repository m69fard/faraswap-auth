# Authentication Service

## Features
- User registration
- User login
- User details

## Documentation

API documentation is available at `/docs`.

## Getting Started

1. **Create a `.env` File**

   In the root of the project, create a `.env` file with the following content:

   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key
   SIGNING_KEY=your-signing-key
   ALLOWED_HOSTS=localhost,127.0.0.1,authentication
   ```
   
   Make sure to replace your-secret-key and your-signing-key with your actual secret and signing keys.


2. **Run the Application**

    Use the following command to build and start the service:

    docker-compose up --build


3. **Test the Application**

    Use the following command to test the service:

    docker compose exec authentication python manage.py test

