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
        base_url = 'https://restcountries.eu/rest/v1/alpha?codes={}'
        if type(self._options) == list:
            self._base_url = base_url.format(';'.join(self._options))
        else:
            base_url = 'https://restcountries.eu/rest/v1/alpha/{}'
            self._base_url = base_url.format(self._options)
        return self

    @property
    def get_country_info_by_country_capital(self):
        base_url = 'https://restcountries.eu/rest/v1/capital/{}'
        self._base_url = base_url.format(self._options)
        return self

    def get_country_info_by_region_or_sub_region(self, reg_or_sub, name):
        if reg_or_sub == 'region':
            base_url = 'https://restcountries.eu/rest/v1/region/{}'
            self._base_url = base_url.format(name)
        elif reg_or_sub == 'sub':
            base_url = 'https://restcountries.eu/rest/v1/subregion/{}'
            self._base_url = base_url.format(name)
        return self

    def get_requested_data(self):
        import requests
        response = requests.get(self._base_url)
        search_results = response.json()
        return search_results

    def print_data(self, search_data):
        print("{:<20} {:<20} {:<15} {:<18} {:<15} {:<15} {:<15} {:<25} {:<15}".format('Country', 'Capital',
                                                          'Region', 'SubReg', 'Population',
                                                          'Area(sqKM)', 'Codes',
                                                          'Currency', 'Lang'))
        for item in search_data:
            try:
                print("{:<20} {:<20} {:<15} {:<18} {:<15d} {:<15f} {:<15s} {:<25s} {:<15s}".format(item['name'],
                                              item['capital'], item['region'],
                                              item['subregion'], int(item['population']),
                                              float(item['area']), str(item['callingCodes']),
                                              str(item['currencies']),str(item['languages'])))
            except TypeError:
                continue


class RefinedSearch(CountryInfoSearch):
    def __init__(self, options, refine_params):
        self._refine_params = refine_params
        super().__init__(options)


def main():
    kenya_data = CountryInfoSearch('africa')
    results = kenya_data.get_country_info_by_region_or_sub_region('region', 'africa').get_requested_data()
    kenya_data.print_data(results)


if __name__ == '__main__':main()