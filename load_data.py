import getpass
import glob
import os

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

password = getpass.getpass("Postgres password: ")

engine = create_engine(
    URL.create(
        "postgresql+psycopg2",
        username="postgres",
        password=password,
        host="localhost",
        port=5432,
        database="olist",
    )
)

# Columns that should be stored as real timestamps, not text
DATE_COLUMNS = {
    "orders": [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ],
    "order_items": ["shipping_limit_date"],
    "order_reviews": ["review_creation_date", "review_answer_timestamp"],
}

for path in sorted(glob.glob("data/*.csv")):
    name = (
        os.path.basename(path)
        .replace("olist_", "")
        .replace("_dataset", "")
        .replace(".csv", "")
    )
    df = pd.read_csv(path, parse_dates=DATE_COLUMNS.get(name, []))
    df.to_sql(name, engine, if_exists="replace", index=False,
              chunksize=5000, method="multi")
    print(f"{name}: {len(df)} rows")