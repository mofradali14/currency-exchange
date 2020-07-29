from unittest import TestCase
from app import app
from converter import ForexConvert
from forex_python.converter import CurrencyRates, CurrencyCodes


class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_home(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_convert(self):
        self.assertEqual(CurrencyRates().convert('USD', 'USD', 1), 1)
        self.assertEqual(CurrencyCodes().get_symbol('USD'), 'US$')
