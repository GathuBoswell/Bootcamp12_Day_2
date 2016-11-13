class CountryInfoSearch(object):
    def __init__(self, options):
        self._base_url = 'https://restcountries.eu/rest/v1/'
        self._options = options

    @property
    def get_url(self):
        return self._base_url

    @property
    def specific_country_info(self):
        base_url = 'https://restcountries.eu/rest/v1/name/{}?fullText=true'
        self._base_url = base_url.format(self._options)
        return self

    @property
    def all_countries_info(self):
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

    def get_country_info_by_region_or_sub_region(self, reg_or_sub):
        if reg_or_sub == 'region':
            base_url = 'https://restcountries.eu/rest/v1/region/{}'
            self._base_url = base_url.format(self._options)
        elif reg_or_sub == 'sub':
            base_url = 'https://restcountries.eu/rest/v1/subregion/{}'
            self._base_url = base_url.format(self._options)
        return self

    def get_requested_data(self):
        import requests
        response = requests.get(self._base_url)
        search_results = response.json()
        return search_results


class RefinedSearch(CountryInfoSearch):
    def __init__(self, options):
        super().__init__(options)
        pass