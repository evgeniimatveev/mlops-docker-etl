import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Select host depending on ENV_MODE
env_mode = os.getenv("ENV_MODE", "local")
db_host = os.getenv("DB_HOST_LOCAL") if env_mode == "local" else os.getenv("DB_HOST_DOCKER")

# Build connection string
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
db = os.getenv("POSTGRES_DB")
url = f"postgresql://{user}:{password}@{db_host}:5432/{db}"

engine = create_engine(url)
print(f"Connecting to → {url}")

# 1. Extract
df = pd.read_csv("data/raw/sales.csv")

# 2. Transform
df["total"] = df["price"] * df["quantity"] * (1 - df["discount"])

# ✅ 3. Load — вставь ЭТО если вдруг вырезал:
df.to_sql("sales", engine, if_exists="replace", index=False)
print("✅ Data successfully loaded into the 'sales' table.")