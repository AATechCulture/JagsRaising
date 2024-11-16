import json

# Load JSON data
with open("MOCK_DATA.json", "r") as file:
    data = json.load(file)

# SQL script generator
values = []
for record in data:
    first_name = f"'{record.get('first_name', 'NULL')}'"
    last_name = f"'{record.get('last_name', 'NULL')}'"
    phone = "NULL"  # Not present in the JSON
    address = f"'{record.get('Adress', 'NULL')}'"
    email = "NULL"  # Not present in the JSON
    situation = "NULL"  # Not present in the JSON
    duration = "NULL"  # Not present in the JSON
    due_date = f"'{record.get('DueDate', 'NULL')}'"
    amount = record.get("Amount", "NULL")

    # SQL-compliant NULL handling
    values.append(
        f"({first_name}, {last_name}, {phone}, {address}, {email}, {situation}, {duration}, {due_date}, {amount})"
    )

# Combine into full SQL script
sql_script = f"INSERT INTO YourTableName (firstName, lastName, phone, address, email, situation, duration, dueDate, amount) VALUES\n"
sql_script += ",\n".join(values) + ";"

# Output the script
with open("insert_script.sql", "w") as output_file:
    output_file.write(sql_script)

print("SQL script generated: insert_script.sql")
