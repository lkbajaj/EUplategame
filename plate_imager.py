# from ChatGPT
from PIL import Image, ImageDraw, ImageFont

# example create a Swedish plate
def create_swedish_plate(number):
    image = Image.open("plate-templates/sweden.png").convert('RGBA')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/DINMittelschriftStd.otf",size=160)

    text = number.replace(" ","  ")
    position = (150,60)
    color = 'black'

    draw.text(position, text, font=font, fill=color)

    image.save(f"plate-outputs/{number}-SW.png")
    image.show()