# Flask + MySQL To‑Do App

A simple two‑tier To‑Do application built with **Flask** and **MySQL**.

- **Frontend + Backend:** Flask  
- **Database:** MySQL  
- Supports both local MySQL and MySQL running inside Docker.  
- Includes basic CRUD: Add, Edit, Toggle Complete, and Delete.

---

## Features

- Add new tasks
- Edit tasks inline
- Mark tasks as completed or incomplete
- Delete tasks
- Schema auto‑initialization via `db-init/init.sql`
- Environment variables managed through `.env`

---

## Project Structure

```
flask-mysql-todo/
├── app.py
├── requirements.txt
├── .env                # Environment variables (not committed)
├── .env.example        # Template for reference
├── templates/
│   └── index.html
└── db-init/
    └── init.sql        # Database schema initialization
```

---

## Prerequisites

- Python 3.9+
- `pip` (Python package manager)
- [Docker](https://www.docker.com/) (optional if you don't have MySQL installed)

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/papani-sivasai/two-tier--flask-app.git
cd two-tier--flask-app
```

---

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv todoEnv
source todoEnv/bin/activate    # On Mac/Linux

# OR on Windows
todoEnv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=my-secret-pw
DB_NAME=todo_db
DB_PORT=3306
```

---

## Option A — Using Local MySQL (Already Installed)

1. Make sure MySQL is running locally.  
2. Initialize the database and table:

```bash
mysql -u root -p < db-init/init.sql
```

3. Ensure `.env` matches your local MySQL credentials.  
4. Run the Flask app:

```bash
python3 app.py
```

Access the app at [http://localhost:5000](http://localhost:5000)

---

## Option B — Using MySQL with Docker (No Local Install)

If you don't have MySQL installed, you can run it in Docker:

```bash
docker run -d   --name todo-mysql   -e MYSQL_ROOT_PASSWORD=my-secret-pw   -e MYSQL_DATABASE=todo_db   -p 3306:3306   -v "$PWD/db-init":/docker-entrypoint-initdb.d:ro   mysql:8.0
```

This will:
- Pull the MySQL image if needed
- Start MySQL on port `3306`
- Initialize the schema from `db-init/init.sql`

Then run the Flask app:

```bash
python3 app.py
```

Access the app at [http://localhost:5000](http://localhost:5000)

### Stop and Remove the MySQL Container

```bash
docker stop todo-mysql
docker rm todo-mysql
```

---

## Testing

- Add new tasks using the form.
- Edit tasks inline.
- Toggle tasks as completed/incomplete.
- Delete tasks.

All operations reflect in the MySQL database.

---

## Environment Variables

| Variable       | Description        | Default         |
|---------------|--------------------|-----------------|
| `DB_HOST`     | MySQL host         | `127.0.0.1`     |
| `DB_USER`     | Database user      | `root`          |
| `DB_PASSWORD` | Database password  | `my-secret-pw` |
| `DB_NAME`     | Database name      | `todo_db`      |
| `DB_PORT`     | MySQL port         | `3306`        |

These are loaded from `.env` using `python-dotenv`.

---

