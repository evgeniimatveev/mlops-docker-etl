# 🧪 MLOps Docker ETL Project – PostgreSQL + Python + SQL CI/CD

![Docker](https://img.shields.io/badge/Docker-Containerized-blue) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue) ![Python](https://img.shields.io/badge/Python-3.10-yellow) ![CI/CD](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-green) ![Status](https://img.shields.io/badge/Status-Active-brightgreen) ![License](https://img.shields.io/badge/License-MIT-lightgrey)

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
│
├── sql/
│   └── dql/                     # SQL queries for analysis
│       ├── daily_sales_trend.sql
│       ├── discount_impact.sql
│       ├── revenue_summary.sql
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
🧰 Technologies Used
🐍 Python 3.10

🐘 PostgreSQL 13 (via Docker)

🐳 Docker & Docker Compose

📦 SQLAlchemy + Pandas (for ETL)

🧽 sqlfluff (for SQL linting and CI/CD)

⚙️ GitHub Actions (for automation)
🧩 ETL Pipeline (etl.py)

Extract – Read raw CSV (sales.csv)

Transform – Calculate total revenue using price, quantity, discount

Load – Write into PostgreSQL table sales

📊 SQL Query Examples
📁 Stored inside: sql/dql/

revenue_summary.sql → Total revenue from all sales

top_categories.sql → Revenue + number of orders by category

sales_by_region.sql → Regional sales breakdown

discount_impact.sql → Impact of applied discounts

daily_sales_trend.sql → Orders and revenue by day

weekly_sales_trend.sql → Weekly performance trend

✨ Ready to plug into Tableau or BI dashboards.



✅ CI/CD: SQL Linting

GitHub Actions automatically runs sqlfluff on every push and pull request:

- name: Lint SQL files
```
run: sqlfluff lint sql/dql --dialect postgres
```
Ensures your SQL queries are always clean and consistent.

#  📦 Run Locally (Docker)

# 1. Build and start containers
```
docker-compose up --build
```
# 2. ETL script will run automatically
```
# You’ll see: "✅ Data successfully loaded into the 'sales' table."
```
# 3. Connect via pgAdmin or any client


## 📜 License  
This project is distributed under the **MIT License**. Feel free to use the code! 🚀  

---

## 📢 Stay Connected!  
💻 **GitHub Repository:** [Evgenii Matveev](https://github.com/evgeniimatveev)  
🌐 **Portfolio:** [Data Science Portfolio](https://www.datascienceportfol.io/evgeniimatveevusa)  
📌 **LinkedIn:** [Evgenii Matveev](https://www.linkedin.com/in/evgenii-matveev-510926276/)  


---

🔥 **If you like this project, don't forget to star ⭐ the repository!** 🔥

