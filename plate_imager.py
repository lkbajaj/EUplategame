# from ChatGPT
from PIL import Image, ImageDraw, ImageFont
import random
import datetime 

EV_CHANCE = 0.25 # chance of a given vehicle being an EV
PLATE_HEIGHT = 250 # height in pixels
SMALLPLATE_WIDTH = 800 # width in pixels
LARGEPLATE_WIDTH = 1250 # width in pixels

smallplate_countries = ['sverige','estland']

# creates the back end of the plates, as in the solutions to the flashcard
def back_matter(plate_number,dictsw):
    country = dictsw['country']
    number = dictsw['number']

    width, height = LARGEPLATE_WIDTH, PLATE_HEIGHT
    size = 60
    if country.lower() in smallplate_countries:
        width = SMALLPLATE_WIDTH
        size = 40
    elif country.lower() in ['bulgarien','bosnien och hercegovina','spanien']: # bulgaria is very big
        size = 50
    
    image = Image.new('RGB', (width,height), color = 'white')
    draw = ImageDraw.Draw(image)

    text = f'land: {country}\nnummer: {number}'
    font = ImageFont.truetype('fonts/Trebuchet MS.ttf', size=size)
    
    bbox = draw.textbbox((0,0),text,font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (width-text_width)//2
    y = (height-text_height)//2

    draw.text((x,y),text, fill = 'black', font = font)
    image.save(f'plate-outputs/{plate_number}-back.png')
    
# example create a Swedish plate
def create_swedish_plate(number):
    image = Image.open("plate-templates/sweden.png").convert('RGBA')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/DINMittelschriftStd.otf",size=170)

    # text = number.replace(" ","  ")
    position = (140,60)
    color = 'black'

    draw.text(position, number, font=font, fill=color)

    image.save(f"plate-outputs/{number}-front.png")
    # image.show()

# could not find a reputable source for what font Ukraine uses on their plates.
# some Redditor mentioned that the closest font to it is Motor4F https://www.reddit.com/r/identifythisfont/comments/ug5e1o/hey_does_anyone_know_where_i_could_get_the/
def create_ukrainian_plate(number):
    image = Image.open("plate-templates/ukrainelg.png").convert('RGBA')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/Motor4F.otf",size=200)

    # text = number.replace(" ","  ")
    position = (220,30)
    color = 'black'

    draw.text(position,number, font=font, fill=color)

    image.save(f"plate-outputs/{number}-front.png")
    # image.show()

# according to Wikipedia, Romania like Sweden uses the DIN 1451 Mittelschrift font
# https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Romania
def create_romanian_plate(number):
    image = Image.open("plate-templates/romanialg.png").convert('RGBA')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/DINMittelschriftStd.otf",size=200)

    # text = number.replace(" ","  ")
    position = (240,70)

    color = 'black'
    if random.random() < EV_CHANCE:
        color = 'green'

    draw.text(position,number, font=font, fill=color)

    image.save(f"plate-outputs/{number}-front.png")
    # image.show()

# I could not find any information for what font Estonia uses for their plates.  From what it looks like, I would suspect they are using the DIN font too.
def create_estonian_plate(number):
    image = Image.open("plate-templates/estonia.png").convert('RGBA')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/DINMittelschriftStd.otf",size=180)

    # text = number.replace(" ","  ")
    position = (130,70)

    color = 'black'

    draw.text(position,number, font=font, fill=color)

    image.save(f"plate-outputs/{number}-front.png")
    # image.show()

def create_bulgarian_plate(number):
    image = Image.open("plate-templates/bulgaria.png").convert('RGBA')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/Bulgarianmarijanovic-Regular.ttf",size=200)

    # text = number.replace(" ","  ")
    position = (200,60)

    color = 'black'
    draw.text(position,number, font=font, fill=color)

    image.save(f"plate-outputs/{number}-front.png")

# Bosnian plates use the FE-Schrift font, as seen by the white line in the 0 
# https://en.wikipedia.org/wiki/European_vehicle_registration_plate#/media/File:License_plate_Bosnia_and_Herzegowina_2009.jpg

def create_bosnian_plate(number):
    image = Image.open("plate-templates/bosnia.png").convert('RGBA')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/FE-FONT.TTF",size=180)

    # text = number.replace(" ","  ")
    position = (140,30)
    color = 'black'

    draw.text(position,number, font=font, fill=color)

    image.save(f"plate-outputs/{number}-front.png")

# Maltese plates use FE-Schrift too
def create_maltese_plate(number):
    image = Image.open("plate-templates/malta.png").convert('RGBA')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/FE-FONT.TTF",size=200)

    # text = number.replace(" ","  ")
    position = (220,30)
    if (number.split())[0] == 'TAXI':
        position = (160,30)
    elif (number.split())[0] == 'POSTA':
        position = (160,50)
        font = ImageFont.truetype("fonts/FE-FONT.TTF",size=170)
    color = 'black'

    draw.text(position,number, font=font, fill=color)

    image.save(f"plate-outputs/{number}-front.png")


# Belgian plates have dark red text (#882329). They use a unique font that I do not want to pay for. The closest thing to it is  DIN1451
def create_belgian_plate(number):
    image = Image.open("plate-templates/belgium.png").convert('RGBA')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/DINMittelschriftStd.otf",size=220)

    position = (180,50)
    color = '#882329'

    draw.text(position,number, font=font, fill=color)

    image.save(f"plate-outputs/{number}-front.png")

# Spain uses a font similar to DIN 1451: https://www.leewardpro.com/articles/licplatefonts/licplate-fonts-eur-2.html#:~:text=Spain,is%20modeled%20after%20DIN%201451.
def create_spanish_plate(number):
    image = Image.open("plate-templates/spain.png").convert('RGBA')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/DINMittelschriftStd.otf",size=220)

    position = (230,50)
    color = 'black'

    draw.text(position,number, font=font, fill=color)

    image.save(f"plate-outputs/{number}-front.png")


# Slovakia uses its own font that I am using a copy developed by /u/Marijanovic on Reddit.
# The Slovakian plates have a seal of the country after the provincial code
def create_slovakian_plate(number):
    image = Image.open('plate-templates/slovakia.png').convert('RGBA')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('fonts/slovakiaMarijanovic.ttf',size=220)
    
    position = (180,40)
    color = 'black'
    draw.text(position,number.split()[0],font=font,fill=color) # province code

    position = (530,40)
    draw.text(position,number.split()[1],font=font,fill=color) # remaining code
    
    image.save(f'plate-outputs/{number}-front.png')

# Cyprus uses FE SCHRIFT. They also have the registration date on the plate in DIN font.
# Since the new series of plates started in 2013 I will make the year from 2013-2025
def create_cypriot_plate(number):
    image = Image.open("plate-templates/cyprus.png").convert('RGBA')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/FE-FONT.TTF",size=200)

    numbertemp = number.replace(' ','  ')

    position = (180,30)
    color = 'black'

    draw.text(position,numbertemp, font=font, fill=color)

    month = str(random.randint(1,12))
    if len(month) == 1:
        month = '0' + month
    
    year = random.randint(13,int(str(datetime.datetime.now().year)[-2:])) 
    registration_text = month + '\n'+ str(year)
    position = (680,120)
    font = ImageFont.truetype("fonts/FE-FONT.TTF",size=50)
    draw.text(position,registration_text, font=font, fill=color)


    image.save(f"plate-outputs/{number}-front.png")
