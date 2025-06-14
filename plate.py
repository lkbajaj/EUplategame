# license plate class
import random
import string
from plate_imager import create_swedish_plate, create_ukrainian_plate

def random_letter():
    return random.choice(string.ascii_uppercase)

def random_number():
    return str(random.randint(0,9))

# Ukraine uses a specific numbering system with cyrillic characters only found in the latin alphabet
# (А, В, Е, І, К, М, Н, О, Р, С, Т, Х) and the first two letters are reserved for regional codes.
# A full list of these codes can be found in "https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Ukraine"
def ukranian_plate_gen():
    legalchars = 'ABEIKMHOPCTX'
    regionalcodes2013 = ['KA','KB','KC','KE','KH','KI','KK','KM','KO','KP',
                         'KT','KX','HA','HB','HC','HE','HH','HI','HK','HM',
                         'HO','HP','HT','HX','IA','IB','IC','IH']
    platenumber = random.choice(regionalcodes2013)
    platenumber = platenumber + " " + random_number() + random_number() + random_number() + random_number()
    platenumber = platenumber + " " + random.choice(legalchars) + random.choice(legalchars)
    return platenumber

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

# Ukraine is another subclass of LicensePlate.
# Ukranian plates are comprised of two letters, a space, four numbers, another space, and two letters e.g: AK 9265 AK
# https://upload.wikimedia.org/wikipedia/commons/7/77/License_plate_of_Ukraine_2015.png 

class Ukraine(LicensePlate):
    def __init__(self):
        country = 'Ukraine'  
        plate_number = ukranian_plate_gen()
        super().__init__(plate_number,country)

    def image_plate(self):
        create_ukrainian_plate(self.plate_number[0])