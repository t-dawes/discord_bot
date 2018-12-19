import requests
from bs4 import BeautifulSoup
#Requires getting a page, parsing and reporting
# Get temperature, feels like, what its like
# No unique URL based on city, crawl and store?
# class="Z0LcW">35.2271° N, 80.8431° W</div>
#
#
# https://en.wikipedia.org/wiki/List_of_population_centers_by_latitude
#
#
# -, first number is south
# -, second number is west

'''
Temp
City
Humidity
Wind
ozone
summary

'''


def get_weather(city):
#   Parse info from web based on city
#   Store values in a list/tuple
    wikiurl = 'https://en.wikipedia.org/wiki/List_of_population_centers_by_latitude'
    o = requests.get(wikiurl)

    # Parse wiki page here for coordinates
    # Take coordinates and translate them for use within dark URL




    darkurl = 'https://darksky.net/forecast/35.2271,-80.8431/us12/en'
    r = requests.get(darkurl)
    data = r.content
    soup = BeautifulSoup(data, 'html.parser')


    # Find values within page
    TEMP = soup.find_all("span", class_= "summary swap")
    CITY = soup.find_all("span", class_= "")
    HUMIDITY = soup.find_all("span", class_= "")
    WIND = soup.find_all("span", class_= "")
    OZONE = soup.find_all("span", class_= "")
    SUMMARY = soup.find_all("span", class_= "")

    return(report)