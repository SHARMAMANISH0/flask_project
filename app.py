from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# MongoDB connection (update the URI as per your configuration)
client = MongoClient("mongodb+srv://manishsharam27:iRCRNnrXgfHRTvoG@pranjal.l25aw.mongodb.net/manish")  # Replace with your MongoDB URI if needed
db = client['manish']  # Database name
users_collection = db['users']  # Collection name
# print("MongoClient")
# Dummy user for testing login
dummy_user = {
    'email': 'manishsharma@gmail.com',
    'password': 'password123'
}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')    
        password = request.form.get('password')

        # Simple check with dummy data
        if email == dummy_user['email'] and password == dummy_user['password']:
            return redirect(url_for('user_details'))
        else:
            flash('Invalid email or password. Please try again.')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/user_details', methods=['GET', 'POST'])
def user_details():
    if request.method == 'POST':
        # Collect user input from the form
        name = request.form.get('name')
        age = request.form.get('age')
        address = request.form.get('address')

        # Insert user details into MongoDB
        user_data = {
            'name': name,
            'age': age,
            'address': address
        }
        users_collection.insert_one(user_data)  # Insert user data into the 'users' collection

        # Return a simple confirmation
        return f"Details submitted! Name: {name}, Age: {age}, Address: {address}"

    return render_template('user_details.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
