import pytest
from city_functions import ciudad_pais

def test_ciudad_pais():
    resultado = ciudad_pais()
    assert resultado == "Santiago, Chile"

test_ciudad_pais()


