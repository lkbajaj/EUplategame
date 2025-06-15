import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # chatGPT method to import outside of the directory

from translator import country_sw
from plate import LicensePlate, Sweden, Ukraine, Romania, Estonia

def test_known_country():
    assert country_sw('Sweden') == 'Sverige'

def test_country_plateclass():
    swedishplate = Sweden()
    country = swedishplate.country
    assert country_sw(country) == 'Sverige'

    romanianplate = Romania()
    country = romanianplate.country
    assert country_sw(country) == 'Rumänien'

    ukranianplate = Ukraine()
    country = ukranianplate.country
    assert country_sw(country) == 'Ukraina'

    estonianplate = Estonia()
    country = estonianplate.country
    assert country_sw(country) == 'Estland'

