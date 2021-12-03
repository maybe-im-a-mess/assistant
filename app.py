from flask import Flask, request, jsonify

import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://www.th-deg.de/de/hochschule/kontakt/fakultaet-ai")
html = BS(r.content, 'html.parser')


app = Flask(__name__)

persons = []

i = 1
for el in html.select(".referat_row > .moreMitarbeiter"):
    name = el.select(".text-overlay > .label_name")
    # room = el.select(".text-overlay > .fa-map-marker-alt")
    # element = {'id': i, 'name': name[0].text, 'room': room[0].text}
    #persons.append(element)
    i += 1


print(persons)


def _find_next_id():
    return max(person["id"] for person in persons) + 1

@app.get("/countries")
def get_countries():
    return jsonify(persons)

@app.post("/countries")
def add_country():
    if request.is_json:
        person = request.get_json()
        person["id"] = _find_next_id()
        persons.append(person)
        return person, 201
    return {"error": "Request must be JSON"}, 415