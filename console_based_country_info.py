class CountryInfoSearch(object):
    def __init__(self, options):
        self._base_url = 'https://restcountries.eu/rest/v1/'
        self._options = options

    @property
    def get_url(self):
        return self._base_url

    @property
    def get_specific_country_info(self):
        base_url = 'https://restcountries.eu/rest/v1/name/{}?fullText=true'
        self._base_url = base_url.format(self._options)
        return self

    @property
    def get_all_countries_info(self):
        if self._options == 'all':
            self._base_url += self._options
            return self

    @property
    def get_country_info_by_calling_code(self):
        base_url = 'https://restcountries.eu/rest/v1/callingcode/{}'
        self._base_url = base_url.format(self._options)
        return self

    @property
    def get_country_info_by_lang(self):
        base_url = 'https://restcountries.eu/rest/v1/lang/{}'
        self._base_url = base_url.format(self._options)
        return self

    @property
    def get_country_info_by_country_currency(self):
        base_url = 'https://restcountries.eu/rest/v1/currency/{}'
        self._base_url = base_url.format(self._options)
        return self

    @property
    def get_country_info_by_country_codes(self):
        base_url = 'https://restcountries.eu/rest/v1/alpha{}'
        if type(self._options) in [list, tuple, set]:
            self._base_url = base_url.format('?codes=' +
                                             ';'.join(self._options))
        else:
            self._base_url = base_url.format('/' + self._options)
        return self

    @property
    def get_country_info_by_country_capital(self):
        base_url = 'https://restcountries.eu/rest/v1/capital/{}'
        self._base_url = base_url.format(self._options)
        return self

    def get_country_info_by_region_or_sub_region(self, reg_or_sub):
        if reg_or_sub == 'region':
            base_url = 'https://restcountries.eu/rest/v1/region/{}'
            self._base_url = base_url.format(self._options)
        elif reg_or_sub == 'subregion':
            base_url = 'https://restcountries.eu/rest/v1/subregion/{}'
            self._base_url = base_url.format(self._options)
        return self

    def get_requested_data(self):
        import requests
        response = requests.get(self._base_url)
        search_results = response.json()
        return search_results

    def print_data(self, search_data):
        print("{:<30} {:<20} {:<15} {:<18} {:<15} {:<15} {:<15} {:<25} {:<10}".format('Country', 'Capital',
                                                          'Region', 'SubReg', 'Population',
                                                          'Area(sqKM)', 'Codes',
                                                          'Currency', 'Lang'))
        if type(search_data) == list:
            for item in search_data:
                print("{:<30.29s} {:<20} {:<15} {:<18} {:<15d} {:<15} {:<15s} {:<25s} {:<10s}".format(item['name'],
                                              item['capital'], item['region'],
                                              item['subregion'], int(item['population']),
                                              str(item['area']), str(item['callingCodes']),
                                              str(item['currencies']),str(item['languages'])))
        elif type(search_data) == dict:
            print("{:<30.29s} {:<20} {:<15} {:<18}"
                  "{:<15d} {:<15} {:<15s} {:<25s} {:<10s}".format(search_data['name'],
                                search_data['capital'], search_data['region'],
                                search_data['subregion'], int(search_data['population']),
                                str(search_data['area']),str(search_data['callingCodes']),
                                str(search_data['currencies']), str(search_data['languages'])))




class RefinedSearch(CountryInfoSearch):
    def __init__(self, options, refine_params):
        self._refine_params = refine_params
        super().__init__(options)


def main():
    kenya_data = CountryInfoSearch('rus')
    results = kenya_data.get_country_info_by_country_codes.get_requested_data()
    kenya_data.print_data(results)


if __name__ == '__main__':main()