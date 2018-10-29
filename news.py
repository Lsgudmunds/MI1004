from newsapi import NewsApiClient
import json

apiKey = "607faf4e6e1f4f868b184da044721073"
userCountry = "us"
newsApi = NewsApiClient(api_key="607faf4e6e1f4f868b184da044721073")
topHeadlines = newsApi.get_top_headlines(sources = "bbc-news")
data = json.dumps(topHeadlines)

print(data)
input("Press enter to end program....")