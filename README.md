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

```plaintext
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

🛠 Technologies Used

Python 3.10

PostgreSQL 13 via Docker

Docker & Docker Compose

SQLAlchemy + Pandas for ETL

sqlfluff (CI/CD for SQL)

GitHub Actions for automation

🧩 ETL Pipeline (etl.py)

Extract – Read raw CSV (sales.csv)

Transform – Calculate total revenue using price, quantity, discount

Load – Write into PostgreSQL table sales

🧪 SQL Query Examples

Inside sql/dql/, you’ll find ready-to-run queries like:

Revenue Summary – total revenue from all sales

Top Categories – by revenue and number of orders

Regional Sales – grouped by region

Discount Analysis – total discount impact

Daily & Weekly Trends – order volumes over time

These are great for dashboards or BI tools (e.g. Tableau).

✅ CI/CD: SQL Linting

GitHub Actions automatically runs sqlfluff on every push and pull request:

- name: Lint SQL files
  run: sqlfluff lint sql/dql --dialect postgres

Ensures your SQL queries are always clean and consistent.

📦 Run Locally (Docker)

# 1. Build and start containers
docker-compose up --build

# 2. ETL script will run automatically
# You’ll see: "✅ Data successfully loaded into the 'sales' table."

# 3. Connect via pgAdmin or any client

🧠 Next Steps



🔗 Author

Your Name  – Data & MLOps Enthusiast🔗 GitHub | LinkedIn

Feel free to fork ⭐ the repo and try the pipeline locally!

