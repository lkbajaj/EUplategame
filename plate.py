# license plate class
import random
import string
from plate_imager import (
    create_swedish_plate, create_ukrainian_plate, create_romanian_plate, 
    create_estonian_plate, create_bulgarian_plate, create_bosnian_plate,
    create_maltese_plate, create_belgian_plate, create_spanish_plate,
    create_slovakian_plate
)
from translator import country_sw, number_sw
from plate_gen import (
    ukranian_plate_gen, romanian_plate_gen, bulgarian_plate_gen,
    maltese_plate_gen, spanish_plate_gen, slovakian_plate_gen
)

def random_letter():
    return random.choice(string.ascii_uppercase)

def random_number():
    return str(random.randint(0,9))

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
    
# Bulgaria is another subclass of LicensePlate.
# Bulgarian plates have a one to two letter regional code, followed by a four digit serial number, and a two letter code called a series
# https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Bulgaria

class Bulgaria(LicensePlate):
    def __init__(self):
        country = 'Bulgaria'
        plate_number = bulgarian_plate_gen()
        super().__init__(plate_number,country)
    
    def image_plate(self):
        create_bulgarian_plate(self.plate_number)
    
    def dict_sw(self):
        countrySW = country_sw(self.country)
        # print(countrySW)
        numarrays =  self.plate_number.split()
        numberSW = numarrays[0] + ' ' + number_sw(int(numarrays[1])) + ' ' + numarrays[2]
        return {'country': countrySW,
                'number': numberSW}
    
# Bosnia and Herzegovina (referred to as Bosnia for simplicity hereonafter) is another subclass of LicensePlate
# Bosnian plates have five numbers and two letters in the order "X00-X-000". There are no regional codes.
#  https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Bosnia_and_Herzegovina

class Bosnia(LicensePlate):
    def __init__(self):
        country = 'Bosnia'
        legalchars = 'AEOJKMT' # only characters represented wqually in Latin and Cyrillic script are used
        plate_number = (
            random.choice(legalchars) + random_number() + random_number() + '-' +
            random.choice(legalchars) + '-' + random_number() + random_number() + random_number()
        )
        
        super().__init__(plate_number, country)
    
    def image_plate(self):
        create_bosnian_plate(self.plate_number)
    
    def dict_sw(self):
        countrySW = country_sw(self.country)
        numarrays = self.plate_number.split('-')
        numberSW = numarrays[0][0] + ' ' + number_sw(int(numarrays[0][1:])) + ' ' + numarrays[1] + ' ' + number_sw(int(numarrays[2]))
        return {'country': countrySW,
                'number': numberSW}
    
# Malta is a subclass of LicensePlate.
# Maltese plates have three letters and three numbers (ZZZ 999). There are no regional codes.
# https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Malta

class Malta(LicensePlate):
    def __init__(self):
        country = 'Malta'
        plate_number = maltese_plate_gen()

        super().__init__(plate_number, country)
    
    def image_plate(self):
        create_maltese_plate(self.plate_number)
    
    def dict_sw(self):
        countrySW = country_sw(self.country)
        numarrays = self.plate_number.split()

        numberSW = ''
        if numarrays[0] == 'TAXI':
            numberSW = numarrays[0] + ' ' +  number_sw(int(numarrays[1][:-1])) + ' ' + numarrays[-1]
            return {'country': countrySW,
                    'number': numberSW}
        
        numberSW = numarrays[0] + ' ' + number_sw(int(numarrays[1]))

        return {'country': countrySW,
                'number': numberSW}


# Belgium is a subclass of LicensePlate
# Limited information for Belgian plates. They use the combination 0-XXX-000
class Belgium(LicensePlate):
    def __init__(self):
        country = 'Belgium'
        plate_number = (
                        random_number() + '-' + random_letter() + random_letter() + random_letter() + '-' +
                        random_number() + random_number() + random_number()
                       )   
        
        super().__init__(plate_number,country)
    
    def image_plate(self):
        create_belgian_plate(self.plate_number)
    
    def dict_sw(self):
        countrySW = country_sw(self.country)
        numarrays = self.plate_number.split('-')

        numberSW = number_sw(int(numarrays[0])) + ' ' + numarrays[1] + ' ' + number_sw(int(numarrays[2]))
        return {'country': countrySW,
                'number': numberSW}
    
# Spain is a subclass of LicensePlate.
# format is 0000 CCC comprising of consanants only. C is a series where the first letter is from A-M as of 2022.
# https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Spain
class Spain(LicensePlate):
    def __init__(self):
        country = 'Spain'
        plate_number = spanish_plate_gen()

        super().__init__(plate_number,country)

    def image_plate(self):
        create_spanish_plate(self.plate_number)
    
    def dict_sw(self):
        countrySW = country_sw(self.country)
        numberSW = number_sw(int(self.plate_number[:4])) + ' ' + self.plate_number[5:]

        return {'country':countrySW,
                'number': numberSW}

# Slovakia is a subclass of LicensePlate
# the format is XX  000XX where the first two letters are a district code and per district
# the sequence goes from AA -> ZZ. The only district to have gotten to ZZ as of now is Bratislava, however,
# for the purpose of this exercise we will make the last two letters random.
class Slovakia(LicensePlate):
    def __init__(self):
        country = 'Slovakia'
        plate_number = slovakian_plate_gen()

        super().__init__(plate_number,country)

    def image_plate(self):
        create_slovakian_plate(self.plate_number)
    
    def dict_sw(self):
        countrySW = country_sw(self.country)
        numarrays = self.plate_number.split(' ')
        numberSW = numarrays[0] + ' ' + number_sw(int(numarrays[1][0:3])) + ' ' + numarrays[1][3:]

        return {'country':countrySW,
                'number':numberSW}