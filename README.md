# 🧪 MLOps Docker ETL Project – PostgreSQL + Python + SQL CI/CD

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Data-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![CI/CD](https://img.shields.io/badge/GitHub_Actions-AutoTest-green?logo=github)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🚀 Overview

This repository demonstrates a **lightweight ETL project** using **Python, PostgreSQL, and Docker** with built-in **CI/CD for SQL validation** via GitHub Actions (`sqlfluff`).

✔ Loads raw sales data → transforms it → stores in PostgreSQL  
✔ Run clean SQL queries from `/sql/dql/`  
✔ SQL linting automatically triggered on push/pull  

---

## 📁 Project Structure

```
mlops_docker_project/
│
├── .conda/                      # Conda environment (optional)
│   └── environment.yaml
│
├── data/
│   ├── raw/                     # Raw CSV input (sales.csv)
│   │   └── sales.csv
│   └── processed/               # Optional processed output
│
├── scripts/                     # Python scripts
│   ├── etl.py                   # ETL logic (extract → transform → load)
│   └── generate_data.py         # Generates sample sales data using Faker
│   └── clean_sql_files.py       # Auto-clean SQL files to pass linting
├── sql/
│   └── dql/                     # SQL queries for analysis
│       ├── daily_sales_trend.sql
│       ├── discount_impact.sql
│       ├── sales_by_region.sql
│       ├── top_categories.sql
│       └── weekly_sales_trend.sql
│
├── .github/workflows/
│   └── sql-lint.yaml            # GitHub Actions config for SQL linting
│
├── docker-compose.yaml          # PostgreSQL + Python setup
├── Dockerfile                   # Python Docker image for ETL
├── .env                         # DB connection credentials
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```
## 🧠 ETL Pipeline

- ✅ **Extract** – Read raw CSV (`sales.csv`)
- ✅ **Transform** – Calculate total revenue using price, quantity, discount
- ✅ **Load** – Write into PostgreSQL table `sales`

---

## 📊 SQL Query Examples (in `sql/dql/`)

- `top_categories.sql` → 🏆 Revenue + order count by category  
- `sales_by_region.sql` → 🌍 Regional breakdown  
- `discount_impact.sql` → 🔻 Impact of discounts  
- `daily_sales_trend.sql` → 📅 Orders & revenue by day  
- `weekly_sales_trend.sql` → 📈 Weekly performance trend  

✔️ These queries are ready to plug into **Tableau, Power BI**, or any BI dashboard

---

## ✅ CI/CD – SQL Linting with GitHub Actions

✔️GitHub Actions automatically runs sqlfluff on every push and pull request:

```
sqlfluff lint sql/dql --dialect postgres
```
Ensures your SQL queries are always clean and consistent. ✨

📦 Run Locally (Docker)
1. Build and start containers
```
docker-compose up --build
```
2. ETL script will run automatically
```
# You’ll see: ✅ Data successfully loaded into the 'sales' table.
```
---

# 📢 Stay Connected!  
💻 **GitHub Repository:** [Evgenii Matveev](https://github.com/evgeniimatveev)  
🌐 **Portfolio:** [Data Science Portfolio](https://www.datascienceportfol.io/evgeniimatveevusa)  
📌 **LinkedIn:** [Evgenii Matveev](https://www.linkedin.com/in/evgenii-matveev-510926276/)  


---

🔥 **If you like this project, don't forget to star ⭐ the repository!** 🔥

