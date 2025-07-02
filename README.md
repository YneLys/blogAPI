# Blog API with JWT Authentication (FastAPI)

## 📌 Overview

This is a RESTful Blog API built with **FastAPI** that supports **JWT-based user authentication**, **post management (CRUD)**, and **admin-restricted user access**. Each user can create, read, update, and delete their own blog posts. Admin users can view all registered users.

---

## 🚀 Features

- User registration with email and password (hashed)
- Login with JWT (access and refresh tokens)
- Secure routes protected by JWT
- Full CRUD for blog posts
- Ownership enforcement: only the post author can edit/delete
- Admin-only access to user data
- SQLAlchemy ORM and Alembic migrations
- SQLite by default (easy to switch to PostgreSQL)
- Automated tests with pytest
- Clean, modular codebase following best practices

---

## 📁 Project Structure

```
blog_api/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   ├── dependencies.py
│   └── routers/
│       ├── auth.py
│       ├── posts.py
│       └── users.py
├── alembic/
├── tests/
│   └── test_posts.py
├── alembic.ini
├── requirements.txt
└── README.md
```

---

## 🧪 Tech Stack

- **FastAPI** for API development
- **SQLAlchemy** as ORM
- **Alembic** for database migrations
- **JWT** with `fastapi-jwt-auth` for secure authentication
- **SQLite** or **PostgreSQL** support
- **Pytest** for testing

---

## ⚙️ Installation

### 1. Clone the repository and install dependencies

```bash
git clone https://github.com/your-username/blog-api.git
cd blog-api
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure environment variables

Create a `.env` file:

```
DATABASE_URL=sqlite:///./test.db
JWT_SECRET_KEY=your_jwt_secret
```

For PostgreSQL:

```
DATABASE_URL=postgresql://user:password@localhost:5432/blogdb
```

### 3. Apply migrations

```bash
alembic upgrade head
```

---

## ▶️ Running the App

```bash
uvicorn app.main:app --reload
```

Access the API at:

- Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔐 Authentication Flow

1. **Register** via `POST /auth/register`
2. **Login** via `POST /auth/login` → returns access + refresh tokens
3. **Include token** in the `Authorization: Bearer <token>` header for protected routes

---

## 📬 API Endpoints

### 🔐 Auth
- `POST /auth/register` – Register a new user
- `POST /auth/login` – Log in and receive tokens

### 📝 Posts (Authenticated)
- `GET /posts/` – List all posts
- `POST /posts/` – Create a post (authenticated)
- `GET /posts/{id}` – View a single post
- `PUT /posts/{id}` – Update own post
- `DELETE /posts/{id}` – Delete own post

### 👤 Users (Admin-only)
- `GET /users/` – List all users
- `GET /users/{id}` – Get user by ID

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🧠 Notes

- Use hashed passwords (`bcrypt`) for security.
- Only authors can modify their posts.
- Admin control is enforced for user routes.
- Suitable for extension with tags, categories, comments, etc.

---

## 📄 License

MIT License
