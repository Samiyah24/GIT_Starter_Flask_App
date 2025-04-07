from application import app
from flask import render_template, url_for, request, redirect, session
from application.person_colourdb import get_people, update_person, get_db_connection


# @app.route('/home')
# def home():
#     return render_template('home.html', title='Home')
# 
# @app.route('/about')
# def about():
#     message = 'This page is dedicated to entering all your favourite colours'
#     return  render_template('about.html', title='About', msg=message)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome_page.html', name=name, group='Group 2')

@app.route('/about')
def about():
    message = 'Our names are Aiman, Sami, Serena, Jhaap, and Khrisha. Welcome to our flower shop'
    return render_template('about.html', title='About us', msg=message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Example validation logic (you can replace this with your real authentication logic)
        if username == "admin" and password == "password":
            return redirect(url_for('home'))  # Redirect to home if credentials are correct
        else:
            return "Login failed. Please check your credentials."

    return render_template('login.html')  # Render the login form on GET request

def send_contact_message(name, email, message):
    print(f"Name: {name}\nEmail: {email}\nMessage: {message}")
    # Additional logic for sending the message or storing it

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process the form submission
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        send_contact_message(name, email, message)  # Function to send message
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/funfacts')
def funfacts():
    return render_template('funfacts.html')

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        fav_color = request.form.get('fav_color')

        # Print the captured values
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Favorite Color (Hex Code): {fav_color}")

        # To displays a success message or handle the data as needed
        return f"Thank you, {first_name} {last_name}! Your favorite color is {fav_color}."
    return render_template('favourite_colour.html')

@app.route('/people_colour')
def all_people_from_db():
    people_from_db = get_people()
    print(people_from_db)
    return render_template('people.html', people=people_from_db, title='List of Peoples Favourite Colour in Database')

@app.route('/update_person/<int:person_id>', methods=['GET', 'POST'])
def update_person_details(person_id):
    # Get a database connection
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch the list of available colours from the 'colour' table
    cursor.execute("SELECT ColourID, Name FROM colour")
    colours = cursor.fetchall()

    if request.method == 'POST':
        new_lastname = request.form['new_lastname']
        new_flowerid = request.form['new_flowerid']

        # Update the person in the database
        update_person(person_id, new_lastname,  new_flowerid)

    # Fetch the person's current information: Lastname and ColourID
    cursor.execute("SELECT Lastname, FlowerID FROM person WHERE PersonID = %s", (person_id,))
    person = cursor.fetchone()

    # Get the current color name based on ColourID
    cursor.execute("SELECT Name FROM flowers WHERE FlowerID = %s", (person[1],))
    current_colour = cursor.fetchone()

    return render_template(
        'update_person.html',
        person_id=person_id,
        flowers=flowers,  # List of all colours passed to template
        person={'Lastname': person[0], 'ColourID': person[1], 'ColourName': current_colour[0]}
    )
