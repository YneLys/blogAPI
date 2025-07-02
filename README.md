# Blog API with JWT Authentication

## Overview

This is a RESTful Blog API built with FastAPI. It allows users to register and log in using JWT authentication, and provides CRUD operations for blog posts. Only authenticated users can create, update, or delete posts, and users can only modify their own content.

## Features

- User registration with email and password (securely hashed)
- JWT-based login and token system (access and refresh tokens)
- CRUD for blog posts
- Permissions: only the post author can update or delete
- SQLAlchemy ORM + Alembic migrations
- SQLite or PostgreSQL support
- Automatic documentation via Swagger and ReDoc
- Unit tests with pytest
- Role-based access with optional admin control

## Project Structure

blog_api/
├── app/
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── crud.py
│ ├── database.py
│ ├── dependencies.py
│ └── routers/
│ ├── auth.py
│ ├── posts.py
│ └── users.py
├── alembic/
├── tests/
│ └── test_posts.py
├── alembic.ini
├── requirements.txt
└── README.md

bash
Copy
Edit

## Setup Instructions

### 1. Clone and install dependencies

```bash
git clone https://github.com/your-username/blog-api.git
cd blog-api
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
2. Configure environment variables
Create a .env file:

ini
Copy
Edit
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your-secret-key
For PostgreSQL:

bash
Copy
Edit
DATABASE_URL=postgresql://user:password@localhost:5432/blogdb
3. Run database migrations
bash
Copy
Edit
alembic upgrade head
4. Start the server
bash
Copy
Edit
uvicorn app.main:app --reload
Access:

Swagger: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

API Endpoints
Auth
POST /auth/register – Create a new user

POST /auth/login – Log in and receive JWT tokens

Posts (Protected)
GET /posts/ – List posts

POST /posts/ – Create a post

GET /posts/{id} – View a post

PUT /posts/{id} – Update (author only)

DELETE /posts/{id} – Delete (author only)

Users (Admin only)
GET /users/ – List all users

GET /users/{id} – Get a single user

Testing
bash
Copy
Edit
pytest
Notes
Ensure the SECRET_KEY is secure in production.

Change the database URL to use PostgreSQL if needed.

Admin user creation can be done using create_admin.py script.

License
MIT License