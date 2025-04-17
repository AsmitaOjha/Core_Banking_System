# 🏦 Laxmi Bank – Core Banking System  
### Transaction & Analytical Data Management  
**Task 2 – ExtensoData Internship**

This project simulates the backend and dashboard of a **Core Banking System** for **Laxmi Bank**, built as part of the **ExtensoData Internship**. It provides both API-based services and a Streamlit-powered analytics dashboard to manage customers, accounts, and financial transactions.

---

## 🚀 Features

- 🔐 Simple and secure User Registration & Authentication  
- 💼 Account Creation and Balance Management  
- 💸 Deposit, Withdraw, and Transfer Operations  
- 📊 Streamlit Dashboard for Real-time Analytics  
- ⚙️ Automated Data Seeding with Faker  
- 📁 SQL Migration Support

---

## 🛠 Tech Stack

- **Python 3.10+**
- **FastAPI** – For RESTful API backend  
- **Streamlit** – For interactive dashboard UI  
- **SQLAlchemy** – Database ORM  
- **SQLite** – Lightweight local DB  
- **Pydantic** – Data validation  
- **Faker** – Randomized test data  
- **Uvicorn** – ASGI server  

---

## 📁 Project Structure
Core_banking_System/
├── .env                         # Environment variables
├── .gitignore                   # Git ignored files
├── app.py                       # Streamlit dashboard and UI
├── automation.py                # Seeds database with Faker
├── database.py                  # DB connection and setup using SQLAlchemy
├── main.py                      # Entry point for FastAPI
├── migration.py                 # SQL migration handler
├── readme.md                    # Project documentation
├── account/
│   ├── account_controller.py    # Account-related route handlers
│   ├── account_schema.py        # Pydantic models for accounts
│   └── account_service.py       # Business logic for accounts
├── auth/
│   ├── auth_controller.py       # Authentication APIs (login/register)
│   └── auth_service.py          # Logic for auth processes
├── transaction/
│   ├── transaction_controller.py # APIs for transaction handling
│   ├── transaction_schema.py     # Pydantic models for transactions
│   └── transaction_service.py    # Core transaction logic
├── user/
│   ├── user_controller.py       # User management APIs
│   ├── user_schema.py           # Data validation for users
│   └── user_service.py          # User service functions
├── migrations/
│   ├── 20250410211847_create_users_table.sql
│   └── <other_timestamped>.sql # Migration scripts
└── venv/                        # Virtual environment

## ▶️ How to Run

### 1. Clone the Repository
https://github.com/AsmitaOjha/Core_Banking_System.git
cd Core_banking_System

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  (activate virtual envrionment)

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run FASTAPI backend
uvicorn main:app --reload

### 5. Run Streamlit dashboard
streamlit run app.py

**📅 Date**
**April 17, 2025**

## 👩‍💻 Author  
**Asmita**  
8th Semester Computer Science Student  
**Task 2 – ExtensoData Internship**

