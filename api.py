import random
import json

def get_list_of_words():
    f= open('names.json')
    data = json.load(f)
    return data

words=get_list_of_words()
random_word = random.choice(words)
print(random_word) 



# import requests
# url = "url"
# iterations = 10000
# for _ in range(iterations):
#     response = requests.get(url)
#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         print(f"Request {_ + 1} successful")
#     else:
#         print(f"Request {_ + 1} failed with status code {response.status_code}")
# print("All requests completed.")