from flask import Flask, render_template, redirect, url_for
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)
app.app_context().push()

app.config["SECRET_KEY"] = "Bum578ble987!"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

connect_db(app)

@app.route('/')
def homepage():
    """ Homepage shows picture of pets with name and availabilty """
    pets = Pet.query.all()
    available_pets = [pet for pet in pets if pet.available]
    unavailable_pets = [pet for pet in pets if not pet.available]
    return render_template('homepage.html', available_pets = available_pets,unavailable_pets = unavailable_pets)

@app.route('/add', methods = ['GET', 'POST'])
def add_pet():
    """ Uses wtform to generate a form for adding Pets"""
    form = PetForm()
    if form.validate_on_submit():
        pet = Pet(name = form.name.data, species = form.species.data, photo_url = form.photo_url.data, age = form.age.data, notes = form.notes.data)
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('homepage'))
    else:
        return render_template('add_pet_form.html', form = form)

@app.route('/<int:pet_id>', methods = ['GET', 'POST'])
def pet_details(pet_id):
    """ Has pet details and uses wtform to edit some of the details"""
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj = pet)

    if form.validate_on_submit():

        pet.name = form.name.data
        pet.species = form.species.data
        pet.age = form.age.data
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(url_for('homepage'))
    else:
        return render_template('pet_details.html', pet = pet, form = form)