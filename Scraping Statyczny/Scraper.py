import requests
from bs4 import BeautifulSoup
import json


req = requests.get('https://www.filmweb.pl/person/Johnny+Depp-29/filmography?profession=actors')

nazwa = 'John Christopher Depp II.json'


zupka= BeautifulSoup(req.text, 'html.parser')

filmy = zupka.find('div', {'class': 'personFilmographySection__container' }) 


# page__container page__navContent showYears
# preview__index
# preview__link
#personFilmographySection__itemInner
# preview previewCard previewFilm PreviewFilm isMini variantAdvertButton variantVod variantBadge variantIndex variantRatings isSpaced showOriginalTitle isReady


kino= []

for filmy1 in filmy.find_all('div', {'class': 'preview__header'}):
    tytuł = filmy1.find('a')
    kino.append(tytuł.text.strip())


# for filmy2 in filmy.find_all('div', {'div': 'preview__index'}):
#     rok = filmy2.find('#text')
#     kino.append(rok.text.strip())


print(kino)

with open(nazwa, 'w', encoding='utf8') as f:
    json.dump(kino, f, ensure_ascii=False)























