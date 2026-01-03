# 📝 Todo List App

A simple and efficient **Todo List Web Application** built using **Flask**.  
This app helps users manage daily tasks — users can **add, update, and delete** tasks with persistent storage using **SQLAlchemy ORM**. The UI is rendered dynamically using **Jinja2 templates**, and the app is lightweight, secure, and production-ready with **Gunicorn**.
<img width="955" height="431" alt="image" src="https://github.com/user-attachments/assets/1254d62c-5a7f-4946-89be-e80e435eb33f" />

---

## 🚀 Features

- ➕ Add new tasks  
- 📝 Update existing tasks  
- ❌ Delete completed/unwanted tasks   
- 🎯 Simple & clean UI  
- ⚡ Lightweight & scalable Flask backend  

---

## 🛠 Tech Stack

**Backend:** Flask  
**Database:** SQLAlchemy ORM  
**Templating:** Jinja2  
**Server:** Gunicorn  

---

## 📂 Project Setup

### 1️⃣ Clone the Repository
```bash
git clone <https://github.com/sandeepyadav73/Todo_List_app>
Todo_List_app
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
```

Activate it:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```bash
python app.py
```

The app will run at:  
👉 http://127.0.0.1:5000/

---

## 🌐 Deployment (Gunicorn)

To run with **Gunicorn**:
```bash
gunicorn app:app
```

---

## 🗄 Database

The project uses **Flask-SQLAlchemy**.  
Task tables are automatically created when the app runs.

---

## 📁 Project Structure

```
📦 Todo_List_app
 ┣ 📁 templates
 ┃ ┗ 📄 base.html
 ┃ ┗ 📄 index.html
 ┃ ┗ 📄 update.html
 ┣ 📁 instance
 ┃ ┗ 📄 todo.db
 ┣ 📄 app.py
 ┣ 📄 requirements.txt
 ┗ 📄 README.md
```


## 📜 License

This project is created for learning and development purposes.

---

### ⭐ If you like this project, don’t forget to give it a star!
