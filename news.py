from newsapi import NewsApiClient
import json

apiKey = "607faf4e6e1f4f868b184da044721073" #API KEY
userCountry = "us" #User country, this should be dynamically genereated by user input.
newsApi = NewsApiClient(api_key=apiKey) #Creates an instance of object NewsApiClient
topHeadlines = newsApi.get_top_headlines(country = userCountry) #Gets top headlines from users country
dataDump = json.dumps(topHeadlines, indent=4, sort_keys=True) #Creates a string of the json dictonary. This is only for test, should be removed later.

for entry in topHeadlines["articles"]: #Prints every title and url for entries in articles.
    print(entry["title"])
    print(entry["url"])
    print()

#print(dataDump)

input("Press enter to end program....")