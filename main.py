from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)


@app.route('/')
def login():
    # This is the home login page
    return render_template("login.html")

@app.route('/', methods=['POST'])
def login_entered():
    # get username and password from user
    username = request.form['username']
    password = request.form['password']
    return render_template("roulette.html")

@app.route('/signup')
def signup():
    # This is the home login page
    return render_template("signup.html")

@app.route('/signup', methods=['POST'])
def signup_entered():
    # get username and password from user
    username = request.form['username']
    password = request.form['password']
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['addressLine1'] + " " + request.form['addressLine2']
    zipcode = request.form['zipcode']
    monthsAtAddress = request.form['monthsAtAddress']
    driversLicenseNumber = request.form['driversLicenseNumber']
    driversLicenseState = request.form['driversLicenseState']
    activeMilitary = request.form['activeMilitary']
    militaryVeteran = request.form['militaryVeteran']
    SSN = request.form['SSN']
    income = request.form['income']
    bankName = request.form['bankName']
    bankAccountType = request.form['bankAccountType']
    bankAccountNumber = request.form['bankAccountNumber']
    employerName = request.form['employerName']
    jobTitle = request.form['jobTitle']

    print(jobTitle)
    return "in"