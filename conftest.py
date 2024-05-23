import pytest
import bun

@pytest.fixture
def kratornaya_bulka():
    name = 'Краторная булка N-200i'
    price = 1255
    return bun.Bun(name, price)