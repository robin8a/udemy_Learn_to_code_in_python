import requests as rq
import json
import pprint as pp

response = rq.get("https://www.google.com")

print ("Type: ", type (response))
print("--------------------------")
print ("Status Code: ", response.status_code)
print("--------------------------")
print ("Headers: ", response.headers)
print("--------------------------")
print ("Headers sub Date: ", response.headers["Date"])
print("--------------------------")
print ("Text: ", response.text)
print("--------------------------")


response = rq.get("https://opentdb.com/api.php?amount=1&category=11&difficulty=easy")
print ("Text: ", response.text)
print("--------------------------")
question  = json.loads(response.text)
print("Question JSON format: ", question)
print("--------------------------")
print("Question JSON pprint format: ", pp.pprint(question))
print("--------------------------")
print(" Category: ", question['results'][0]['category'])
print(" Question: ", question['results'][0]['question'])
print("--------------------------")
print("--------------------------")
# Dictionary to String
person = {'Name': 'Robin', 'Age': 40, 'Gender': 'Male'}
print ("Person Dictionary format: ", person)
person_json = json.dumps(person)
print ("Person json format: ", person_json)
print("--------------------------")


