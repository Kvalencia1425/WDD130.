#KURT VALENCIA UNIT CONVERTER TEST FILE

from unit_converter import convert_meter_to_km, convert_meter_to_ft,convert_cm_to_in, convert_celsius_to_fahrenheit, convert_fahrenheit_to_celsius,convert_kg_to_lbs, convert_lbs_to_kg, convert_liter_to_gallon, convert_gallon_to_liter
from pytest import approx 
import pytest


def test_convert_meter_to_kilometer():

    assert convert_meter_to_km(5000) == approx(5.0)
    assert convert_meter_to_km(2500) == approx(2.5)
    assert convert_meter_to_km(1000) == approx(1.0)

def test_convert_meter_to_ft():

    assert convert_meter_to_ft(50) == approx(164.04, abs=0.1)
    assert convert_meter_to_ft(100) == approx(328.08, abs=0.1)
    assert convert_meter_to_ft(5000) == approx(16404.20, abs=0.1)

def test_convert_cm_to_in():

    assert convert_cm_to_in(150) == approx(59.0551, abs=0.1)
    assert convert_cm_to_in(200) == approx(78.7402, abs=0.1)
    assert convert_cm_to_in(500) == approx(196.85, abs=0.1)

def test_convert_celsius_to_fahrenheit():

    assert convert_celsius_to_fahrenheit(37) == approx(98.6, abs=0.1)
    assert convert_celsius_to_fahrenheit(40) == approx(104, abs=0.1)
    assert convert_celsius_to_fahrenheit(100) == approx(212, abs=0.1)

def test_convert_fahrenheit_to_celsius():

    assert convert_fahrenheit_to_celsius(100) == approx(37.7778, abs=0.1)
    assert convert_fahrenheit_to_celsius(150) == approx(65.5556, abs=0.1)
    assert convert_fahrenheit_to_celsius(200) == approx(93.3333, abs=0.1)

def test_convert_kg_to_lbs():

    assert convert_kg_to_lbs(82) == approx(180.779, abs=0.1)
    assert convert_kg_to_lbs(63) == approx(138.891, abs=0.1)
    assert convert_kg_to_lbs(45) == approx(99.208, abs=0.1)

def test_convert_lbs_to_kg():

    assert convert_lbs_to_kg(170) == approx(77.1107, abs=0.1)
    assert convert_lbs_to_kg(115) == approx(52.1631, abs=0.1)
    assert convert_lbs_to_kg(100) == approx(45.3592, abs=0.1)

def test_convert_gallon_to_liter():

    assert convert_gallon_to_liter(90) == approx(340.687, abs=0.1)
    assert convert_gallon_to_liter(10) == approx(37.8541, abs=0.1)
    assert convert_gallon_to_liter(5) == approx(18.9271, abs=0.1)

def test_convert_liter_to_gallon():

    assert convert_liter_to_gallon(20)== approx(5.28344, abs=0.1)
    assert convert_liter_to_gallon(15)== approx(3.96258, abs=0.1)
    assert convert_liter_to_gallon(10)== approx(2.64172, abs=0.1)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])