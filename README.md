# User Management System

A RESTful user management backend built with Django and MongoEngine (MongoDB).

---

## Features

- Built with Django 4.2 and Django REST Framework
- Uses MongoDB as a backend via `mongoengine`
- Dockerized for easy deployment
- REST APIs to manage users (CRUD)

---

## Quick Start (with Docker)

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/user-management.git
cd user-management
```

### 2. Build and Run the Containers
```bash
docker compose up -d --build
```

- The Django app will be available at: [http://localhost:8000](http://localhost:8000)
- MongoDB runs on port `27017` internally.

### 3. Stop the Containers

```bash
docker compose down
```

---

## Environment Configuration

MongoDB connection is set using environment variables:

| Variable    | Description         | Default      |
|-------------|---------------------|--------------|
| `MONGO_DB`  | MongoDB database    | `userdb`     |
| `MONGO_HOST`| MongoDB host name   | `mongo`      |
| `MONGO_PORT`| MongoDB port        | `27017`      |

These are defined in `docker-compose.yml`.

---

## REST API Endpoints

All endpoints accept and return JSON.

### 📥 Create a New User

- **URL:** `POST /api/user`
- **Body:**
  ```json
  {
    "message": "User registered successfully",
    "user": { 
      "first_name": "John",
      "last_name": "Doe",
      "email": "john@test.com",
      "phone": "1234567891"
    }
  }
  ```
- **Success Response:** `201 Created`

---

### 📤 Get All Users

- **URL:** `GET /api/users`
- **Response:**
  ```json
  [
    { "id": "...", 
      "first_name": "John",
      "last_name": "Doe", 
      "email": "john@test.com",
      "phone": "..." 
    },
    {
      ...
    } 
  ]
  ```

---

### 🔍 Get User by ID

- **URL:** `GET /api/user/<id>`
- **Example:** `/api/user/1`
- **Response:**
  ```json
  { 
    "id": "...", 
    "first_name": "John",
    "last_name": "Doe", 
    "email": "john@test.com",
    "phone": "..." 
  }
  ```

---

### ✏️ Update User by ID

- **URL:** `PUT /api/user/update/<id>`
- **Body:**
  ```json
  {
    "last_name": "Smith"
  }
  ```

---

### ❌ Delete User by ID

- **URL:** `DELETE /api/user/delete/<id>`

---