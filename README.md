# HNG Stage 0 Backend Task

This is a simple public API built with Python and Flask that returns basic information in JSON format.

## API Documentation

### Endpoint
- **URL**: `https://firstflaskproject-63zs.onrender.com`
- **Method**: `GET`

### Response Format
```json
{
   "email": "your-email@example.com",
   "current_datetime": "2025-01-30T09:30:00Z",
   "github_url": "https://github.com/yourusername/hng-stage0-api"
}
```

## Features
- Returns a JSON response containing:
  - Your registered email address.
  - The current datetime in **ISO 8601 UTC format**.
  - The GitHub repository URL of the project.
- CORS enabled for cross-origin access.
- Lightweight and fast API response time (< 500ms).

## Setup Instructions

### Clone the Repository
```sh
git clone https://github.com/yourusername/hng-stage0-api.git
cd hng-stage0-api
```

### Install Dependencies
Make sure you have Python installed, then run:
```sh
pip install -r requirements.txt
```

### Run the Application Locally
```sh
python app.py
```

### Deploying the API
To deploy this API, you can use platforms like **Render, Vercel, Heroku, or AWS Lambda**.

## Acceptance Criteria

### Functionality
- The API must accept **GET requests** and return the required JSON response.
- The `current_datetime` field must be dynamically generated in **ISO 8601 format (UTC)**.
- Provides appropriate **HTTP status codes**.

### Code Quality
- Well-structured and maintainable code.
- Proper error handling.

### Documentation
- **README.md** must include:
  - A clear description of the project.
  - Setup instructions for running locally.
  - API documentation, including:
    - Endpoint URL.
    - Request/response format.
    - Example usage.

### Deployment
- The API must be deployed to a publicly accessible endpoint.
- The API should have a **fast response time** (< 500ms).

## Backlinks
- [HNG Python Developers](https://hng.tech/hire/python-developers)
- [HNG C# Developers](https://hng.tech/hire/csharp-developers)
- [HNG Go Developers](https://hng.tech/hire/golang-developers)
- [HNG PHP Developers](https://hng.tech/hire/php-developers)
- [HNG Java Developers](https://hng.tech/hire/java-developers)
- [HNG Node.js Developers](https://hng.tech/hire/nodejs-developers)

