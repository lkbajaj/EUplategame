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

print(country_sw('Sweden'))
print(country_sw('sweden'))
print(country_sw('belarus'))