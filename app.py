from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!'

@app.route('/information')
def info():
    return 'Flask is the micro-framework of choice for building Machine Learning API endpoints'

@app.route('/profile/<name>')
def profile(name):
    return f"This is the profile information for {name.upper()}"


personnel = {
    "rachel": "Executive Vice President of Managerial Functions",
    "wallace": "Senior Vice President of Managerial Functions",
    "rosie": "Staff Vice President of Managerial Functions",
    "james": "Vice Vice President of Managerial Functions",
    "henri": "Junior Vice President of Managerial Functions"
}

@app.route('/personnel/<name>')
def personnel_lookup(name):
    if name in personnel:
        return f"{personnel[name].upper()}"
    else:
        return f"{name} is not part of the group"


@app.route('/employee-search')
def employee_search():
    name = request.args.get('name')
    age = request.args.get('age')
    return f"I searched for employees named {name} who are {age} years old"


if __name__ == '__main__':
    app.run(port=5001)  # Ensure you are running on port 5001 if that's what you want

