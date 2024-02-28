# Name : Siva Rama Rohan Sunkarapalli
# Section : CS591
# Homework : 5

import requests

# Greeting endpoint
response = requests.get('http://127.0.0.1:5000/api/greeting', params={'name': 'John'})
data = response.json()
print(data['message'])

# Sum endpoint
response = requests.get('http://127.0.0.1:5000/api/sum', params={'a': 2, 'b': 3})
data = response.json()
print(f"Sum of 2 and 3: {data['result']}")

# Countries endpoint
response = requests.get('http://127.0.0.1:5000/api/countries')
data = response.json()
print("List of countries:")
for country in data['countries']:
    print(country)
