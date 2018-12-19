import requests
import bs4

# return first sentence and link 
def get_wiki():
    url = "https://en.wikipedia.org/wiki/Special:Random"
    r = requests.get(url)
    return

