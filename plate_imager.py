# from ChatGPT
from PIL import Image, ImageDraw, ImageFont
import random

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