from flask import Flask, render_template, request
import sqlite3
import os

# Get the current working directory
currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

# Route for the home page
@app.route("/")
def main():
    return render_template("index.html", message="")  # Render the main page

# Route for adding a car entry
@app.route("/", methods=['POST'])
def add_car():
    try:
        # Retrieve form data
        brand = request.form['Brand']
        price = request.form['Price']
        body = request.form['Body']
        mileage = request.form['Mileage']
        engine_v = request.form['EngineV']
        engine_type = request.form['EngineType']
        registration = request.form['Registration']
        year = request.form['Year']
        model = request.form['Model']

        # Connect to the SQLite database
        db_path = os.path.join(currentdirectory, "car_sales.db")
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Insert data into the database
        query = """
        INSERT INTO car_sales (brand, price, body, mileage, engine_v, engine_type, registration, year, model)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (brand, price, body, mileage, engine_v, engine_type, registration, year, model))
        connection.commit()
        connection.close()

        # Return to the main page with a success message
        return render_template("index.html", message="Car details added successfully!")
    except Exception as e:
        return render_template("index.html", message=f"Error: {e}")

# Route for the About page
@app.route("/about")
def about():
    return render_template("about.html")  # Render the About page

# Route for the Data page
@app.route("/data")
def data():
    try:
        # Connect to the SQLite database
        db_path = os.path.join(currentdirectory, "car_sales.db")
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Retrieve the most recent 7 rows from the car_sales table
        query = "SELECT * FROM car_sales ORDER BY id DESC LIMIT 7"
        result = cursor.execute(query).fetchall()
        connection.close()

        # Render the Data page with the results
        return render_template("data.html", results=result)
    except Exception as e:
        return render_template("data.html", results=[], error=f"Error: {e}")


if __name__ == "__main__":
    app.run(debug=True)
