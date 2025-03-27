🧪 MLOps Docker Project: ETL + PostgreSQL + SQL Analysis

This project demonstrates a lightweight ETL pipeline in Python, fully containerized with Docker, and connected to PostgreSQL for data storage and SQL-based analysis.

It also features CI/CD integration with GitHub Actions to validate SQL queries using sqlfluff.

🚀 Project Highlights

🐳 Dockerized ETL Workflow – Load sales data from CSV → transform → insert into PostgreSQL

🐘 PostgreSQL – Stores structured sales data for analytics

🧠 SQL DQL Queries – For generating insights like revenue, trends, categories

✅ CI/CD – SQL validation on push/pull via GitHub Actions

📁 Clean Project Structure – Modular and scalable layout for real-world MLOps setups

📂 Project Structure

mlops_docker_project/
│
├── .conda/                   # 📌 Conda environment config (local)
│   └── environment.yaml
│
├── data/                    
│   ├── raw/                  # 📂 Raw CSV input data
│   │   └── sales.csv
│   └── processed/            # 🧪 (Optional) processed data placeholder
│
├── docker/                  
│   ├── docker-compose.yaml   # 🐘 PostgreSQL + Python config
│   └── Dockerfile            # 🛠 Docker image for ETL script
│
├── scripts/                 
│   ├── etl.py                # 🔁 Main ETL pipeline script
│   └── generate_data.py      # 🧪 Data generator (using Faker)
│
├── sql/                     
│   └── dql/                  # 📊 SQL queries for analysis
│       ├── daily_sales_trend.sql
│       ├── discount_impact.sql
│       ├── revenue_summary.sql
│       ├── sales_by_region.sql
│       ├── top_categories.sql
│       └── weekly_sales_trend.sql
│
├── .github/workflows/       
│   └── sql-lint.yaml         # ✅ GitHub Action for SQL linting
│
├── .env                     # 🔐 PostgreSQL credentials & config
├── requirements.txt         # 📦 Python dependencies
└── README.md                # 📘 Project documentation

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

