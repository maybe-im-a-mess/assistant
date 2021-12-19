from flask import Flask, request, jsonify
import json
import requests
from bs4 import BeautifulSoup as BS

# Parse the information about the professors from the web site of the university
r = requests.get("https://www.th-deg.de/de/hochschule/kontakt/fakultaet-ai")
html = BS(r.content, 'html.parser')


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

# Load the information about professors to the json file
filename = 'persons.json'
with open(filename, "w", encoding="UTF-8") as file:
    json.dump(persons, file, indent=2, ensure_ascii=False)
