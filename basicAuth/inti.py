
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Hardcoded users and passwords
users = {
    "admin": "password123",
    "user1": "mypassword"
}

# Verify password function
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

# Protect this route with authentication
@app.route('/protected')
@auth.login_required
def protected():
    return jsonify({"message": f"Hello, {auth.current_user()}! You have accessed a protected route."})

@app.route('/')
def public():
    return "Welcome to the public page! No login required."

if __name__ == '__main__':
    app.run(debug=True,port=5000 )

