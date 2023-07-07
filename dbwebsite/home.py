import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",  # Replace with your MySQL server host
    user="root",   # Replace with your MySQL username
    password="destined",  # Replace with your MySQL password
    database="dbwebsite"  # Replace with your MySQL database name
)

# Create a cursor
cursor = db.cursor()

# Create the table if it doesn't exist
create_table = "CREATE TABLE IF NOT EXISTS test (email VARCHAR(50) not null,password varchar(50) not null);"
cursor.execute(create_table)
db.commit()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    password = request.form['password']
    try:
        # Insert the email into the table
        insert_query = f"INSERT INTO test(email,password) VALUES ('{email}','{password}');"
        cursor.execute(insert_query)
        db.commit()
        print("Data added successfully")
    except mysql.connector.Error as error:
        print("Error inserting data into MySQL database:", error)

    return "Youv'e logged successfully"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
