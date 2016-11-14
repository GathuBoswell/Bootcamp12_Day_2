class CountryInfoSearch(object):
    def __init__(self, options):
        self._base_url = 'https://restcountries.eu/rest/v1/'
        self._options = options

    @property
    def get_url(self):
        return self._base_url

    @property
    def get_specific_country_info(self):
        '''Url for specific country search '''
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
        try:
            response = requests.get(self._base_url)
            search_results = response.json()
            return search_results
        except requests.ConnectionError:
            search_results = {'status':'ConnectionError! internet connection'}
            return search_results


    def print_data(self, search_data):
        if type(search_data) == dict:
            try:
                if search_data['status'] in [404, 'ConnectionError! internet connection']:
                    print('Data for {} Not Found !!, "{} Error"'.format(self.get_url, search_data['status']))
                    return ('Data for {} Not Found !! "{} Error"'.format(self.get_url, search_data['status']))
            except KeyError:
                pass

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
    def __init__(self, options, un_refined_data):
        # takes search data to be refined as argument
        self._un_refined_data = un_refined_data
        super().__init__(options)

    def refine_search_by_currency(self, currency):
        # should handle type checking for the currency
        # and all errors that would result
        return currency

    def refine_search_by_region(self, region):
        # should handle type checking for the region
        # and all errors that would result
        return region

    def refine_search_by_subregion(self, subregion):
        # should handle type checking for the subregion
        # and all errors that would result
        return subregion

    def refine_search_by_capital(self, capital):
        # should handle type checking for the capital
        # and all errors that would result
        return capital

    def refine_search_by_lang(self, lang):
        # should handle type checking for the lang
        # and all errors that would result
        return lang

    def get_refined_data(self, refine_param):
        '''Handles all refining of data, any number of times its called'''
        refined_data = []
        if type(self._un_refined_data) == list:
            for item in self._un_refined_data:
                if item[refine_param]:
                    refined_data.append(item)
        elif type(self._un_refined_data) == dict:
            if self._un_refined_data[refine_param]:
                refined_data.append(self._un_refined_data)
            else:
                return 'Data being searched for not found'
        return refined_data



def main():
    kenya_data = CountryInfoSearch('260')
    results = kenya_data.get_country_info_by_calling_code.get_requested_data()
    kenya_data.print_data(results)


if __name__ == '__main__':main()