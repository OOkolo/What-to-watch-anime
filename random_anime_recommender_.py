# -*- coding: utf-8 -*-
"""Random Anime Recommender .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b47tpNJEtiCH8jKTwjsA8rQz-L-WTtau
"""

#Import the modules we'll use
import numpy as np
import requests
from bs4 import BeautifulSoup
from IPython.display import Image
print("import done")

"""# Random Anime Generator
---
**Choosing a new anime is always emotional torure**
**This anime generator takes some of the stress out of the decision.**
****************
I have scraped *MyAnimeList.net*'s top airing page and come up with a function to take the titles on the top airing page and generate a random one. 

All that is required of the user is to copy and paste the link from either page 1,2,3, *or* n to get a random title generated

"""

#Define the function to generate the random title
def rando(anime_list):
    """Takes a list/array item and returns a title based on a randomly generated number
    that corressponds with the item's index"""
    #establish a range based on the length of the list
    list_range= np.arange(0, (len(anime_list)))
    random_index= np.random.choice(list_range)
    return anime_list[random_index]
Image(filename="Myanimelist.png")

print("Please paste the URL from MyAnimeList.net's 'Top Anime' page")
my_anime_link = input()
#The input should only take links from the myanimelist.com "top airing" pages. 
#either page 1,2,4,.....n
src = requests.get(str(my_anime_link))
print(src.status_code)
site= src.content
site_soup= BeautifulSoup(site, "lxml")

anime_titles=[]
headers= site_soup.find_all("h3")
for link in headers:
    only_title= link.find("a")
    title= only_title.text
    anime_titles.append(title)

print(anime_titles)

#Drop "More" items that also have the h3 tags
    #Use a try and except line here because there are definitely less "more" items than the entire length of the loop
    #but they often vary with page, so it's best to just iterate through as many times as possible until they all drop
try:
    for item in anime_titles:
        anime_titles.remove("More")
except:

    print("All is well, carry on")

print(anime_titles)

rando(anime_titles)

rando(anime_titles)

rando(anime_titles)

