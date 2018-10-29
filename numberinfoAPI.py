import json
import urllib3

hej = "hej"
url = "http://numbersapi.com/"
number = input("Enter a number...")
http = urllib3.PoolManager()
numberTrivia = http.request('GET', url+"/"+number+"/trivia")
numberTriviaDecoded = numberTrivia.data.decode('UTF-8')

print(numberTriviaDecoded)
print(hej)
input('Press enter to continue...')
