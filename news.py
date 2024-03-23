# import requests
# from bs4 import BeautifulSoup


# url = 'https://www.livelaw.in/articles/top-stories/justice-ram-kumar-comprehensive-analysis-bharatiya-nagarik-suraksha-sanhita-2023-252551'
# reqs = requests.get(url)
# soup = BeautifulSoup(reqs.text, 'html.parser')

# urls = []
# for link in soup.find_all('a'):
# 	print(link.get('href'))

from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='83da63a881a5458a998df46998f0d8e5')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='legal',
                                          sources='livelaw',
                                          category='legal',
                                          language='en',
                                          country='in')



# /v2/top-headlines/sources
sources = newsapi.get_sources()