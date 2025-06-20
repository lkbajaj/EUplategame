import random
import string

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

# Like other countries whose main language uses the Cyrillic alphabet (Ukraine) only a subset of characters in both cyrllic and latin letters are adopted
# For Bulgaria it is А, В, Е, К, М, Н, О, Р, С, Т, У, Х. I am using a custom font though from /u/Marijanovic on reddit that uses a Y instead of the cyrllic counterpart
# The series (last two letters) only uses nine letters (no E,O,Y) https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Bulgaria
def bulgarian_plate_gen():
    serieschars = 'ABKMHPCTX'
    serieschars_sofia = 'ABEKMHPCTX' # until 2023 E was only reserved for cars in Sofia

    provincecodes = ['A','B','BH','BP','E','EB','EH','K','M','H','OB',
                     'P','PA','PB','PK','PP','C','CA','CB','CH','CM',
                     'CO','CC','CT','T','TX','Y','X']
    
    provincecode = random.choice(provincecodes)
    series = ''
    if provincecode in ['C','CA','CB']: # this car is registered in Sofia
        series = series + random.choice(serieschars_sofia) + random.choice(serieschars_sofia)
        while series == 'EE': # this is reserved for trailers and caravans
            series = '' + random.choice(serieschars_sofia) + random.choice(serieschars_sofia)
    else:
        series = series + random.choice(serieschars) + random.choice(serieschars)
    
    return provincecode +  ' ' + random_number() + random_number() + random_number() + random_number() + ' ' + series

# Maltese plates use latin characters with no restrictions from A-Z in the three letter, three number system (ZZZ 999)
# https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Malta
# For privately owned vehicles the first
def maltese_plate_gen():
    SPECIAL_NUMBER_PROB = 0.05
    if random.random() < SPECIAL_NUMBER_PROB:
        # inspired by https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Malta
        special_numbers = ['TAXI','TR','POSTA','GVP','BUS','GVX']
        numberchoice = random.choice(special_numbers)
        if numberchoice == 'TAXI':
            MG = 'MG'
            return 'TAXI ' + random_number() + random_number() +  random.choice(MG)
        if numberchoice == 'TR':
            return 'TR ' + random_number() + random_number() + random_number() + random_number()
        if numberchoice == 'POSTA': 
            numberchoice = numberchoice + ' '
            numi = random.randint(1,4)
            for i in range(numi):
                numberchoice = numberchoice + random_number()
            
            return numberchoice

        return numberchoice + ' ' + random_number() + random_number() + random_number()
    
    return (
        random_letter() + random_letter() + random_letter() + ' ' +
        random_number() + random_number() + random_number()
    )

# Spanish plates use four digits a space and then a counter, which uses consonants 
# B,C,D,F,G,H,J,K,L,M,N,P,R,S,T,V,W,X,Y,Z 
# As of 2022, the series is up to beginning with M
def spanish_plate_gen():
    legalchars = 'BCDFGHJKLMNPRSTVWXYZ'
    legalchars_beg = 'BCDFGHJKLM'

    return (
        random_number() + random_number() + random_number() + random_number() + ' ' +
        random.choice(legalchars_beg) + random.choice(legalchars) + random.choice(legalchars)
    )

# Slovakian plates do the XX NNNXX where the first two letters are a provinicial code and the last two letters
# correspond to the a series from AA -> ZZ
def slovakian_plate_gen():
    district_codes = ['BA','BD','BE','BI','BL','BT','BB','BC','BK','BJ','BN','BR','BS','BY','CA',
                      'CA','DK','DS','DT','GA','GL','HC','HE','IL','KA','KE','KC','KI','KK','KM',
                      'KN','KS','LC','LE','LM','LV','LL','MA','MI','ML','LV','LL','MA','MI','ML',
                      'MT','MY','NR','NI','NT','NM','NO','NZ','NC','PB','PD','PE','PK','PN','PO',
                      'PV','PS','PP','PT','PU','RA','RK','RS','RV','SA','SB','SC','SE','SI','SK',
                      'SL','SN','SO','SP','SV','TT','TA','TB','TN','TC','TE','TO','TR','TS','TS',
                      'TV','VK','VT','ZA','ZI','ZL','ZC','ZH','ZM','ZV']
    district = random.choice(district_codes)

    return district + ' ' + random_number() + random_number() + random_number() + random_letter() + random_letter()

# Cypriate plates have 3 letters a space and 3 numbers. 
# The three letters follow a sequence from AAA, AAB, ..., ZZZ. Since the introduction,
# of new plates in 2013 the sequence started at M. 
# Only the following letters are used: ABEHKMNPTXYZ.  https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Cyprus
def cypriot_plate_gen():
    legalchars = 'ABEHKMNPTXYZ'
    legalchars_beg = 'MNPTXYZ'

    return (
        random.choice(legalchars_beg) + random.choice(legalchars) + random.choice(legalchars) + ' ' 
        + random_number() + random_number() + random_number()
    )