import requests
import bs4

res = requests.get('https://www.interia.pl/')

site = bs4.BeautifulSoup(res.text, 'html.parser')

# parent section class="news-section"
print(site.find_all("ul", id="facts_news_small"))   #Małe
lista = site.find_all("ul", id="facts_news_small")
print(type(lista))
'''
print("-------------------------------------------------------------------------------------------------------------")
x = []
for line in site.find_all("ul", id="facts_news_small"):
    x.append(line)
print(x[0])
print("-------------------------------------------------------------------------------------------------------------")
print(x[0].find_all("a", {"class": "news-a"}))
print("-------------------------------------------------------------------------------------------------------------")

jakos tak trzeba to sobie rozbic
'''

print("\n\n")
print(site.find_all("div", id="facts_news_small_one"))  # Obrazek w małych faktach
print("\n\n")
print(site.find_all("ul", id="facts_photos"))  #male fakty z malymi obrazkami

print("\n\n\n\n")
#Duze fakty section id="titles"

print(site.find("ul", id="tiles_karuzela"))

#Maly Biznes section id="buisness" / podobne jak male fakty
print("\n\n\n\n")
print(site.find_all("div", id="business_news_one"))  # biznes z obrazkiem
print("\n\n")
print(site.find("ul", id="business_news"))  #biznes bez obrazków

#Sport
#maly div class="sport-left"
print("\n\n\n\n")
print(site.find_all("div", id="sport_news_one"))  # obrazek sport lewo
print("\n\n")
print(site.find_all("ul", id="sport_news"))  # male niusy bez obrazka
print("\n\n")

# duzy div class="sport-right"
print("\n\n\n\n")
print(site.find_all("div", {"class": "sport-right"}))  # duzy sport

#maly obrazkowy sport ul id="sport_bottom_photos"
print("\n\n\n\n")
print(site.find_all("ul", id="sport_bottom_photos"))

#the end



