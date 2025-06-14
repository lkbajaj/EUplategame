# license plate class
import random
import string
from plate_imager import create_swedish_plate

def random_letter():
    return random.choice(string.ascii_uppercase)

def random_number():
    return str(random.randint(0,9))

class LicensePlate:
    def __init__(self,plate_number,country):
        self.plate_number = plate_number,
        self.country = country,
        self.vehicle = 'car' # making every vehicle a car for now. May add support to bikes in the future.
    
    # basic to-string method. Goal to create code that generates a picture of the plate eventually
    def __str__(self):
        return (f'number: {self.plate_number},country:{self.country},vehicle:{self.vehicle}')
    
# Sweden is a subclass of LicensePlate. I have included a constructor method for this purpose.
# Swedish plates are comprised of three letters a space and three numbers e.g: WNF 864.
# They also use the DIN 1451 font https://en.wikipedia.org/wiki/DIN_1451.
class Sweden(LicensePlate):
    def __init__(self):
        country = 'Sweden' # duh
        plate_number = random_letter() + random_letter() + random_letter() + " " + random_number() + random_number() + random_number()
        super().__init__(plate_number,country)

    def image_plate(self):
        create_swedish_plate(self.plate_number[0])

