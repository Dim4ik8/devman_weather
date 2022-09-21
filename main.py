import requests

list_of_places = ['london', 'svo', 'cherepovets']

response_london = requests.get("https://wttr.in/london?lang=ru&M&n&q&T")

for place in list_of_places:
    print(requests.get(f"https://wttr.in/{place}?lang=ru&M&n&q&T").text)