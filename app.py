from flask import Flask, request, jsonify

import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://www.th-deg.de/de/hochschule/kontakt/fakultaet-ai")
html = BS(r.content, 'html.parser')

app = Flask(__name__)

persons = []

infos = []

for el in html.select(".referat_row > .moreMitarbeiter"):
    for para in el.find_all("p"):
        infos.append(para.get_text())

profs = [infos[i:i + 5]
         for i in range(0, len(infos), 5)]

for i in range(len(profs)):
    profs[i].pop(1)
    profs[i].pop(2)
    profs[i].pop(2)
    element = {'id': i + 1, 'name': profs[i][0], 'room': profs[i][1]}
    persons.append(element)

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
