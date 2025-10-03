# 📝 Flask + MySQL To-Do App

A simple **two-tier To-Do application** built with **Flask** and **MySQL**.

- 📌 **Frontend + Backend:** Flask  
- 🗄️ **Database:** MySQL  
- 🐳 Optionally run MySQL in Docker (no local install required)  
- ✍️ Supports **Add**, **Edit**, **Toggle Complete**, and **Delete** tasks

---

## 🚀 Features

- ✅ Add new to-dos  
- ✍️ Edit existing tasks inline  
- ☑️ Mark tasks as completed / incomplete  
- 🗑 Delete tasks  
- 📄 Schema auto-initialization via `db-init/init.sql`  
- 🔐 Secrets managed through `.env` file

---

## 📦 Project Structure

flask-mysql-todo/
├── app.py
├── requirements.txt
├── .env # Environment variables (not committed)
├── templates/
│ └── index.html
└── db-init/
  └── init.sql # Database schema initialization

## 🧰 Prerequisites

- Python 3.9+
- `pip` (Python package manager)
- [Docker](https://www.docker.com/) (optional, if you don't have MySQL installed)

---

## ⚡ Getting Started

1️⃣ Clone the Repository

```bash
git clone https://github.com/papani-sivasai/two-tier--flask-app.git
cd two-tier--flask-app

2️⃣ Create and Activate Virtual Environment

python3 -m venv todoEnv
source todoEnv/bin/activate    # On Mac/Linux
# OR
todoEnv\Scripts\activate       # On Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup Environment Variables

Create a .env file in the project root:

DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=my-secret-pw
DB_NAME=todo_db
DB_PORT=3306

🗄 Option A — Use Local MySQL (If Already Installed Locally)

1️⃣ Make sure MySQL is running locally.
2️⃣ Create the database and table using the SQL script:

mysql -u root -p < db-init/init.sql

3️⃣ Update .env to match your local MySQL credentials.
4️⃣ Run the Flask app using:

```bash
python3 app.py


The app should now be available at:
👉 http://localhost:5000

🐳 Option B — Use MySQL via Docker (No Local MySQL Needed)

If you don’t have MySQL installed, you can run it in Docker:

docker run -d \
  --name todo-mysql \
  -e MYSQL_ROOT_PASSWORD=my-secret-pw \
  -e MYSQL_DATABASE=todo_db \
  -p 3306:3306 \
  -v "$PWD/db-init":/docker-entrypoint-initdb.d:ro \
  mysql:8.0


✅ This:

Pulls the MySQL image if not available

Starts MySQL on port 3306

Automatically initializes the schema from db-init/init.sql

Then run the Flask app:

python3 app.py


Open: 👉 http://localhost:5000

🧹 To stop and clean up MySQL container
docker stop todo-mysql && docker rm todo-mysql

