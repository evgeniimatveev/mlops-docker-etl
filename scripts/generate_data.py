import pandas as pd
import random
from faker import Faker
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()
fake = Faker()

rows = int(os.getenv("NUM_ROWS", 500))

categories = ["electronics", "fashion", "books", "home", "toys"]
regions = ["North America", "Europe", "Asia", "South America", "Africa"]

def generate_row():
    price = random.randint(100, 1200)
    quantity = random.randint(1, 10)
    discount = round(random.uniform(0.05, 0.30), 2)  # 5% to 30%

    return {
        "product": fake.word(),
        "category": random.choice(categories),
        "price": price,
        "quantity": quantity,
        "discount": discount,
        "buyer": fake.name(),
        "date": fake.date_between(start_date="-2y", end_date="today"),
        "region": random.choice(regions)
    }

data = [generate_row() for _ in range(rows)]
df = pd.DataFrame(data)

os.makedirs("data/raw", exist_ok=True)
df.to_csv("data/raw/sales.csv", index=False)

print(f"✅ Generated {rows} rows with extra fields → data/raw/sales.csv")