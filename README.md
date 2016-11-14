# Bootcamp12_Day_2

This repo contains the following tasks for boot camp day two:
- [x] [Word Count lab](https://github.com/GathuBoswell/Bootcamp12_Day_2/blob/master/word_count.py)
- [x] [Max and Min lab](https://github.com/GathuBoswell/Bootcamp12_Day_2/blob/master/max_min_number.py)
- [x] [ Http and Web lab](https://github.com/GathuBoswell/Bootcamp12_Day_2/blob/master/console_based_country_info.py)

#### console_based_country_info.py 
is a console app to return country
or countries data from [Rest Countries API](http://restcountries.eu/)
Depending on several search criteria as follows;
* All countries info - will return info for all countries
* Specific Country info - info for one country
* Calling Codes
* Region
* Subregion
* Capital city
* Country code, e.g 'ke' for Kenya
* calling code, e.g '254' for Kenya
* ISO 639-1 Language e.g 'en', for English

It has two parts;
- [x] Simple Interface
- [ ] Advance Interface - for data refining (Not fully implemented)

###### Usage:

When the program is run, it presents the user with choices;

```
         Welcome to Country info Data Search   
         ###################################
     Please select a Search criteria choice below:

1. By country name
2. By country code
3. "all" for all countries
4. By region
5. By subregion
6. By capital city
7. By Calling code
8. By ISO 639-1 Language e.g "en", for English


Enter Your Choice:_
```

_*Sample output*_

```
         Welcome to Country info Data Search

         ###################################

     Please select a Search criteria choice below:

1. By country name
2. By country code
3. "all" for all countries
4. By region
5. By subregion
6. By capital city
7. By Calling code
8. By ISO 639-1 Language e.g "en", for English


Enter Your Choice:6
Enter The country Capital City: nairobi



Country    Capital     Region    SubReg          Population   Area(sqKM)   Codes    Currency    Lang
Kenya      Nairobi     Africa    Eastern Africa  46050000     580367.0     ['254']   ['KES']    ['en', 'sw']
```

