import unittest

from console_based_country_info import CountryInfoSearch

class CountryInfoTestCase(unittest.TestCase):
    def test_Info_instance(self):
        countries_bordering_morocco = CountryInfoSearch('all')
        self.assertEqual(type(countries_bordering_morocco), CountryInfoSearch)

    def test_all_countries_info(self):
        countries_bordering_morocco = CountryInfoSearch('all')
        self.assertEqual(countries_bordering_morocco.all_countries_info(), 'https://restcountries.eu/rest/v1/all')

    def test_specific_country_data(self):
        kenya_data = CountryInfoSearch('name/Kenya?fullText=true')
        all_kenya_data = kenya_data.specific_country_info.get_requested_data()
        self.assertEqual(all_kenya_data[0]['name'], 'Kenya', msg='The country should be `Kenya`')


if __name__ == '__main__':
    unittest.main()
