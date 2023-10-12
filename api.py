import random
import json
import sys
import requests

def get_list_of_words():
    f= open('names.json')
    data = json.load(f)
    return data

words=get_list_of_words()
try:
    print("arg 1",sys.argv[1],"arg 2",sys.argv[2]) 
except IndexError:
    print("Some arguments are missing")

try:
    count = int(sys.argv[2])
except:
    print("Second argument must be number")

iterations = count
for _ in range(iterations):
    random_word = random.choice(words)
    url = sys.argv[1]+"?text="+random_word
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(f"Request {_ + 1} successful "+url)
    else:
        print(f"Request {_ + 1} failed with status code {response.status_code}")
print("All requests completed.")