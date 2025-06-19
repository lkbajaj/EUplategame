import yaml

# gives the Swedish translation of a country (string). List of supported countries read by swedish-translations/countries.yaml
def country_sw(country):
    country = country.lower()
    with open('swedish-translations/countries.yaml') as file:
        data = yaml.safe_load(file)
    
    data = data['countries']
    if country not in data:
        return None 
     
    return data[country]

# supports up to four digit numbers. May handle more in the future if necessary
def number_sw(num):
     # check if number is even an int
    if not isinstance(num, int) or isinstance(num, bool):
        return None
    
    if num == 0:
        return 'noll'
    
    with open('swedish-translations/numbers.yaml') as file:
        data = yaml.safe_load(file)
    data = data['numbers']
    
    if num > 9999: # current limit. May extend for very long plates
        return None 
    elif num == 100:
        return data['hundreds'][100]
    elif num == 1000:
        return data['thousands'][1000]
    # maybe I can loop number by number and remove a digit each time 
    
    returnstr = ''
    while num >= 1:
        firstdigit = int(str(num)[0])
        if num >= 1000:
            returnstr = returnstr + data['ones'][firstdigit] + ' '
            returnstr = returnstr + data['thousands'][1000] + ' '
        elif num >= 100:
            returnstr = returnstr +  data['ones'][firstdigit]
            if firstdigit == 1:
                returnstr = returnstr + ' ' # add the space for the one

            returnstr = returnstr + data['hundreds'][100] + ' '
        elif num >= 20:
            tens = int(str(firstdigit) + '0')
            returnstr = returnstr + data['tens'][tens]
        elif num > 9 and num < 20:
            tens = num 
            returnstr = returnstr + data['tens'][num]
            return returnstr # return here because there's not going to be anything else
        else: # a number that is in the ones' place
            return returnstr + data['ones'][num]

        num = int(str(num)[1:]) # continue looping by sheering off the first digit
    
    if returnstr[-1] == ' ':
        returnstr = returnstr[0:-1]

    return returnstr
            
            
