from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


# Function to connect to your existing SQLite database
def get_db_connection():
    conn = sqlite3.connect(
        "CostOfLiving.db"
    )  # Ensure this points to your existing database
    conn.row_factory = sqlite3.Row
    return conn


# API endpoint to add an expense
@app.route("/add_expense", methods=["POST"])
def add_expense():
    try:
        # Parse incoming JSON data
        data = request.json

        # Extract fields from the JSON payload
        name = data.get("Name")
        last_name = data.get("LastName")
        address = data.get("Address")
        electricity_due_date = data.get("ElectricityDueDate")
        electricity_amount = data.get("ElectricityAmount")
        water_due_date = data.get("WaterDueDate")
        water_amount = data.get("WaterAmount")
        gas_due_date = data.get("GasDueDate")
        gas_amount = data.get("GasAmount")
        internet_due_date = data.get("InternetDueDate")
        internet_amount = data.get("InternetAmount")
        rent_due_date = data.get("RentDueDate")
        rent_amount = data.get("RentAmount")
        groceries_cost = data.get("GroceriesCost")
        transportation_cost = data.get("TransportationCost")
        healthcare_cost = data.get("HealthcareCost")
        other_expenses = data.get("OtherExpenses")
        total_monthly_expenses = data.get("TotalMonthlyExpenses")

        # Validate required fields
        required_fields = [
            name,
            last_name,
            address,
            electricity_due_date,
            electricity_amount,
            water_due_date,
            water_amount,
            gas_due_date,
            gas_amount,
            internet_due_date,
            internet_amount,
            rent_due_date,
            rent_amount,
            groceries_cost,
            transportation_cost,
            healthcare_cost,
            other_expenses,
            total_monthly_expenses,
        ]

        if any(field is None for field in required_fields):
            return jsonify({"error": "All fields are required."}), 400

        # Insert the data into the database (exclude 'id')
        conn = get_db_connection()
        conn.execute(
            """
            INSERT INTO Expenses (
                Name, LastName, Address,
                ElectricityDueDate, ElectricityAmount,
                WaterDueDate, WaterAmount,
                GasDueDate, GasAmount,
                InternetDueDate, InternetAmount,
                RentDueDate, RentAmount,
                GroceriesCost, TransportationCost,
                HealthcareCost, OtherExpenses,
                TotalMonthlyExpenses
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                name,
                last_name,
                address,
                electricity_due_date,
                electricity_amount,
                water_due_date,
                water_amount,
                gas_due_date,
                gas_amount,
                internet_due_date,
                internet_amount,
                rent_due_date,
                rent_amount,
                groceries_cost,
                transportation_cost,
                healthcare_cost,
                other_expenses,
                total_monthly_expenses,
            ),
        )
        conn.commit()
        conn.close()

        # Return success response
        return jsonify({"message": "Expense added successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/add_medical", methods=["POST"])
def add_medical():
    try:
        # Parse incoming JSON data
        data = request.json

        # Extract fields from the JSON payload
        first_name = data.get("firstName")
        last_name = data.get("lastName")
        phone = data.get("phone")
        address = data.get("address")
        email = data.get("email")
        situation = data.get("situation")
        duration = data.get("duration")
        due_date = data.get("dueDate")
        amount = data.get("amount")

        # Validate required fields
        required_fields = [
            first_name,
            last_name,
            phone,
            address,
            email,
            situation,
            duration,
            due_date,
            amount,
        ]

        if any(field is None for field in required_fields):
            return jsonify({"error": "All fields are required."}), 400

        # Insert the data into the database
        conn = get_db_connection()
        conn.execute(
            """
            INSERT INTO Medical (
                firstName, lastName, phone, address, email, 
                situation, duration, dueDate, amount
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                first_name,
                last_name,
                phone,
                address,
                email,
                situation,
                duration,
                due_date,
                amount,
            ),
        )
        conn.commit()
        conn.close()

        # Return success response
        return jsonify({"message": "Medical data added successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/add_studentf", methods=["POST"])
def add_studentf():
    try:
        # Parse incoming JSON data
        data = request.json

        # Extract fields from the JSON payload
        first_name = data.get("firstName")
        last_name = data.get("lastName")
        phone = data.get("phone")
        address = data.get("address")
        email = data.get("email")
        situation = data.get("situation")
        duration = data.get("duration")
        due_date = data.get("dueDate")
        amount = data.get("amount")

        # Validate required fields
        required_fields = [
            first_name,
            last_name,
            phone,
            address,
            email,
            situation,
            duration,
            due_date,
            amount,
        ]

        if any(field is None for field in required_fields):
            return jsonify({"error": "All fields are required."}), 400

        # Insert the data into the database
        conn = get_db_connection()
        conn.execute(
            """
            INSERT INTO StudentTuitionForm (
                firstName, lastName, phone, address, email, 
                situation, duration, dueDate, amount
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                first_name,
                last_name,
                phone,
                address,
                email,
                situation,
                duration,
                due_date,
                amount,
            ),
        )
        conn.commit()
        conn.close()

        # Return success response
        return jsonify({"message": "Tuition data added successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/add_food", methods=["POST"])
def add_food():
    try:
        # Parse incoming JSON data
        data = request.json

        # Extract fields from the JSON payload
        first_name = data.get("firstName")
        last_name = data.get("lastName")
        phone = data.get("phone")
        address = data.get("address")
        email = data.get("email")
        situation = data.get("situation")
        duration = data.get("duration")
        due_date = data.get("dueDate")
        amount = data.get("amount")

        # Validate required fields
        required_fields = [
            first_name,
            last_name,
            phone,
            address,
            email,
            situation,
            duration,
            due_date,
            amount,
        ]

        if any(field is None for field in required_fields):
            return jsonify({"error": "All fields are required."}), 400

        # Insert the data into the database
        conn = get_db_connection()
        conn.execute(
            """
            INSERT INTO FoodForm (
                firstName, lastName, phone, address, email, 
                situation, duration, dueDate, amount
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                first_name,
                last_name,
                phone,
                address,
                email,
                situation,
                duration,
                due_date,
                amount,
            ),
        )
        conn.commit()
        conn.close()

        # Return success response
        return jsonify({"message": "Food data added successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/add_shelter", methods=["POST"])
def add_shelter():
    try:
        # Parse incoming JSON data
        data = request.json

        # Extract fields from the JSON payload
        first_name = data.get("firstName")
        last_name = data.get("lastName")
        phone = data.get("phone")
        address = data.get("address")
        email = data.get("email")
        situation = data.get("situation")
        duration = data.get("duration")
        due_date = data.get("dueDate")
        amount = data.get("amount")

        # Validate required fields
        required_fields = [
            first_name,
            last_name,
            phone,
            address,
            email,
            situation,
            duration,
            due_date,
            amount,
        ]

        if any(field is None for field in required_fields):
            return jsonify({"error": "All fields are required."}), 400

        # Insert the data into the database
        conn = get_db_connection()
        conn.execute(
            """
            INSERT INTO ShelterForm (
                firstName, lastName, phone, address, email, 
                situation, duration, dueDate, amount
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                first_name,
                last_name,
                phone,
                address,
                email,
                situation,
                duration,
                due_date,
                amount,
            ),
        )
        conn.commit()
        conn.close()

        # Return success response
        return jsonify({"message": "shelter data added successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
