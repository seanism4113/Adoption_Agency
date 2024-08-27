from models import Pet, db
from app import app

db.drop_all()
db.create_all()

pet1 = Pet(name = 'Shelly', 
           species = 'dog', 
           photo_url = 'https://imgc.allpostersimages.com/img/posters/lynn-m-stone-portrait-of-yellow-labrador-retriever-female-in-early-morning-light-by-red-zinnias-geneva_u-l-q10vmon0.jpg' , 
           age = 12,
           notes = "Cutest Dog Ever")

pet2 = Pet(name = 'Gus', 
           species = 'dog', 
           photo_url ='https://www.purina.co.uk/sites/default/files/styles/square_medium_440x440/public/2022-07/Clumber-Spaniel.jpg', 
           age = 6,
           notes = "Goes by Gusarooni")

pet3 = Pet(name = 'Moonshine', 
           species = 'cat', 
           photo_url = 'https://www.catster.com/wp-content/uploads/2023/11/bombay-cat-on-the-grass_Viktor-Sergeevich_Shutterstock.jpg' , 
           age = 16, 
           notes = "Meow",
           available = False)

pet4 = Pet(name = 'Sonic', 
           species = 'porcupine', 
           photo_url = 'https://i.pinimg.com/736x/41/5e/cd/415ecd7accd9f1aea5dac9006b475c04.jpg', 
           age = 12,
           notes = "Super Fast, Super Cuddly")

pet5 = Pet(name = 'Nips', 
           species = 'cat', 
           photo_url = 'https://static.vecteezy.com/system/resources/thumbnails/022/963/918/small_2x/ai-generative-cute-cat-isolated-on-solid-background-photo.jpg', 
           age = 5,
           notes = "That is one Cool Cat!")

db.session.add_all([pet1,pet2,pet3,pet4,pet5])
db.session.commit()


