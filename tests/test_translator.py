import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # chatGPT method to import outside of the directory

from translator import country_sw, number_sw
from plate import Sweden, Ukraine, Romania, Estonia, Bulgaria, Malta, Belgium, Spain, Cyprus

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

    bulgarianplate = Bulgaria()
    country = bulgarianplate.country
    assert country_sw(country) == 'Bulgarien'

    malteseplate = Malta()
    country = malteseplate.country
    assert country_sw(country) == 'Malta'

    belgianplate = Belgium()
    country = belgianplate.country
    assert country_sw(country) == 'Belgien'

    spanishplate = Spain()
    country = spanishplate.country
    assert country_sw(country) == 'Spanien'

    cypriotplate = Cyprus()
    country = cypriotplate.country
    assert country_sw(country) == 'Cypern'

    assert cypriotplate.dictsw['country'] == 'Cypern' # yay new system works

def test_unknown_country():
    assert country_sw('Mali') is None

def test_number_ones():
    assert number_sw(8) == 'åtta'
    assert number_sw(4) == 'fyra'
    assert number_sw(1) == 'ett'

def test_number_tens():
    assert number_sw(12) == 'tolv'
    assert number_sw(14) == 'fjorton'
    assert number_sw(50) == 'femtio'
    assert number_sw(70) == 'sjuttio'
    assert number_sw(int('060')) == 'sextio'

def test_number_hundreds():
    assert number_sw(100) == 'hundra'
    assert number_sw(500) == 'femhundra'
    assert number_sw(1000) == 'tusen'
    assert number_sw(2000) == 'två tusen'

def test_misc_numbers():
    assert number_sw(42) == 'fyrtiotvå'
    assert number_sw(67) == 'sextiosju'
    assert number_sw(211) == 'tvåhundra elva'
    assert number_sw(106) == 'ett hundra sex'
    assert number_sw(624) == 'sexhundra tjugofyra'
    assert number_sw(1010) == 'ett tusen tio'
    assert number_sw(2169) == 'två tusen ett hundra sextionio'
    assert number_sw(0) == 'noll'

def test_unknown_numbers():
    assert number_sw(12.56) is None
    assert number_sw('ninety five') is None
    assert number_sw(False) is None
    assert number_sw([23]) is None