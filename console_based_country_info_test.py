import unittest

from console_based_country_info import CountryInfoSearch

class CountryInfoTestCase(unittest.TestCase):
    def test_Info_instance(self):
        countries_bordering_morocco = CountryInfoSearch('all')
        self.assertEqual(type(countries_bordering_morocco), CountryInfoSearch)

    def test_all_countries_info(self):
        countries_bordering_morocco = CountryInfoSearch('all')
        self.assertEqual(countries_bordering_morocco.all_country_info(), 'https://restcountries.eu/rest/v1/all')

    def test_specific_country_data(self):
        all_kenya_data = CountryInfoSearch('Kenya')


if __name__ == '__main__':
    unittest.main()
