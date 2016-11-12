class CountryInfoSearch(object):
    def __init__(self, options):
        self._base_url = 'https://restcountries.eu/rest/v1/'
        self._options = options

    def all_countries_info(self):
        if self._options == 'all':
            self._base_url += self._options
            return self._base_url

    @property
    def specific_country_info(self):
        self._base_url += self._options
        return self

    def get_requested_data(self):
        import requests
        response = requests.get(self._base_url)
        search_results = response.json()
        return search_results