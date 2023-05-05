import requests

response = requests.get("http://universities.hipolabs.com/search?country=Latvia")
data = response.json()

sorted_universities = sorted(data, key=lambda k: k["name"])

for uni in sorted_universities:
    print(uni["name"])