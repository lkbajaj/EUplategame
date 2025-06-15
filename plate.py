# license plate class
import random
import string
from plate_imager import create_swedish_plate, create_ukrainian_plate, create_romanian_plate, create_estonian_plate
from translator import country_sw, number_sw

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

# Like Ukraine, the first two letters are reserved for regional codes. The list can be found in https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Romania
def romanian_plate_gen():
    legalchars  = 'ABCDEFGHIJKLMNOPRSTUVWXYZ' # Q is not allowed since it may be confused with O
    legalchars_start = 'ABCDEFGHJKLMNPRSTUVWXYZ' # may not start with I or O to avoid confusion with 1 and 0
    regionalcodes = ['B','AB','AG','AR','BC','BH','BN','BR','BT','BV','BZ','CJ','CL','CS',
                     'CT','CV','DB','DJ','GJ','GL','GR','HD','HR','IF','IL','IS','MH','NT',
                     'OT','PH','SB','SJ','SM','SV','TL','TM','TR','VL','VN','VS']
    
    platenumber = random.choice(regionalcodes)
    # if the plate is from Bucharest (code "B") then three numbers are used instead of the usual two
    if platenumber == 'B':
        platenumber = platenumber + " " + random_number() + random_number() + random_number()
    else:
        platenumber = platenumber + " " + random_number() + random_number() 
    
    platenumber = platenumber + " " + random.choice(legalchars_start) + random.choice(legalchars) + random.choice(legalchars)
    while platenumber[-3:] == ('JEG' or 'BOU'): # JEG means crash in Romanian and BOU means dumb so they are not allowed
        platenumber = platenumber[:-3] + random.choice(legalchars_start) + random.choice(legalchars) + random.choice(legalchars)
    
    return platenumber

class LicensePlate:
    def __init__(self,plate_number,country):
        self.plate_number = plate_number
        self.country = country
        self.vehicle = 'car' # making every vehicle a car for now. May add support to bikes in the future.
    
    # basic to-string method. Goal to create code that generates a picture of the plate eventually
    def __str__(self):
        return (f'number: {self.plate_number},country:{self.country},vehicle:{self.vehicle}')
    
    # dict of all properties translated to Swedish. On every country to implement different translations
    def dict_sw(self):
        return {}
    
# Sweden is a subclass of LicensePlate. I have included a constructor method for this purpose.
# Swedish plates are comprised of three letters a space and three numbers e.g: WNF 864.
# They also use the DIN 1451 font https://en.wikipedia.org/wiki/DIN_1451.
class Sweden(LicensePlate):
    def __init__(self):
        country = 'Sweden' # duh
        plate_number = random_letter() + random_letter() + random_letter() + " " + random_number() + random_number() + random_number()
        super().__init__(plate_number,country)

    def image_plate(self):
        create_swedish_plate(self.plate_number)

    def dict_sw(self):
        countrySW = country_sw(self.country)
        numberSW = self.plate_number[0:4] + number_sw(int(self.plate_number[4:]))
        return {'country':countrySW,
                'number':numberSW}

# Ukraine is another subclass of LicensePlate.
# Ukranian plates are comprised of two letters, a space, four numbers, another space, and two letters e.g: AK 9265 AK
# https://upload.wikimedia.org/wikipedia/commons/7/77/License_plate_of_Ukraine_2015.png 

class Ukraine(LicensePlate):
    def __init__(self):
        country = 'Ukraine'  
        plate_number = ukranian_plate_gen()
        super().__init__(plate_number,country)

    def image_plate(self):
        create_ukrainian_plate(self.plate_number)
    
    def dict_sw(self):
        countrySW = country_sw(self.country)
        numberSW = self.plate_number[0:3] + number_sw(int(self.plate_number[3:6])) + self.plate_number[7:]
        return {'country':countrySW,
                'number':numberSW}  


# Roamania is another subclass of LicensePlate.
# Romanian plates are comprised of two letters, a space, two numbers, another space, and three letters. e.g: BN 18 CTL
# https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Romania. 
class Romania(LicensePlate):
    def __init__(self):
        country = 'Romania'
        plate_number = romanian_plate_gen()
        super().__init__(plate_number,country)

    def image_plate(self):
        create_romanian_plate(self.plate_number)
    
    def dict_sw(self):
        countrySW = country_sw(self.country)
        numarrays = self.plate_number.split()
        numberSW = numarrays[0] + ' ' + number_sw(int(numarrays[1])) + ' ' + numarrays[2]
        return {'country':countrySW,
                'number':numberSW}



# Estonia is another subclass of LicensePlate.
# The most common Estonian license plate type is A1, which is comprised of three numbers, followed by a space, and three letters. Just like Sweden.
class Estonia(LicensePlate):
    def __init__(self):
        country = 'Estonia'
        plate_number = random_letter() + random_letter() + random_letter() + " " + random_number() + random_number() + random_number()
        super().__init__(plate_number,country)

    def image_plate(self):
        create_estonian_plate(self.plate_number)

    def dict_sw(self): 
        countrySW = country_sw(self.country)
        numberSW = self.plate_number[0:4] + number_sw(int(self.plate_number[4:]))
        return {'country': countrySW,
                'number': numberSW}