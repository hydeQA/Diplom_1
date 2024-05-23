

class TestBuns:
    def test_get_buns_name(self, kratornaya_bulka):
        assert kratornaya_bulka.get_name() == 'Краторная булка N-200i'

    def test_get_price(self, kratornaya_bulka):
        assert kratornaya_bulka.get_price() == 1255
