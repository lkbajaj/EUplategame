import sys
import os
import yaml
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # chatGPT method to import outside of the directory

import pytest
import plate_imager

with open('swedish-translations/countries.yaml') as file:
    data = yaml.safe_load(file)

countries = list(data['countries'].keys())

@pytest.mark.parametrize("country", countries)
def test_create_plate_function_exists(country):
    func_name = f'create_{country.lower()}_plate'
    assert hasattr(plate_imager, func_name), f"Missing function: {func_name}"
    assert callable(getattr(plate_imager, func_name)), f"{func_name} is not callable"