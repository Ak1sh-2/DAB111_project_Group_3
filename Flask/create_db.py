import sqlite3
import pandas as pd
import os

def create_database():
    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_directory, 'car_sales.db')

    # Connect to SQLite (or create it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the table (with columns for car sales data)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS car_sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT,
        price INTEGER,
        body TEXT,
        mileage FLOAT,
        engine_v FLOAT,
        engine_type TEXT,
        registration TEXT,
        year INTEGER,
        model TEXT
    )
    ''')
    conn.commit()

    # Load the dataset from CSV
    csv_path = r"H:\Data Analytics for Business SEM 3\Intro to python\DAB111 python\flask\data\Car_sales_dataset.csv"
    data = pd.read_csv(csv_path)

    # Insert data into the table
    for index, row in data.iterrows():
        cursor.execute('''
        INSERT INTO car_sales (brand, price, body, mileage, engine_v, engine_type, registration, year, model)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (row['Brand'], row['Price'], row['Body'], row['Mileage'], row['EngineV'], row['Engine Type'], row['Registration'], row['Year'], row['Model']))

    conn.commit()
    conn.close()
    print("Database created and data inserted successfully!")

if __name__ == "__main__":
    create_database()
