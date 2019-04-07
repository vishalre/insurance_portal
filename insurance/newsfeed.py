

from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='e894820c96e44c209a7be606a4ffdcf6')

# /v2/top-headlines
import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=e894820c96e44c209a7be606a4ffdcf6')
response = requests.get(url).json()
print(response)
article = response['articles']

results = []
for ar in article:
    results.append(ar['title'])

# for i in range(len(results)):
#
#         # printing all trending news
#     print(i + 1, results[i])
