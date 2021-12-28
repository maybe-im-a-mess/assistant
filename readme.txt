Campus Navigation “Solik”

Kurzbeschreibung: Das System hilft bei der Suche von allen Büros und Räumlichkeiten des Campus der THD sowie bei der Suche nach Professoren für die Fakultät für Angewandte Informatik und informiert über das aktuelle Wetter in Deggendorf.

Installationsbeschreibung:

1. Rasa installieren:
	- Erstellen Sie eine neue virtuelle Umgebung, indem Sie einen Python-Interpreter auswählen und ein .\\venv-Verzeichnis erstellen, um es zu speichern. Befehl für Windows: C:\> python3 -m venv ./venv
	- Aktivieren Sie die virtuelle Umgebung. C:\> .\venv\Scripts\activate
	- Installieren Sie Rasa Open Source mit pip (erfordert Python 3.7 oder 3.8). C:\> pip3 install -U --user pip && pip3 install rasa
2. Das Projekt klonen:
https://github.com/maybe-im-a-mess/assistant.git
3. Betreten Sie den Ordner mit dem Projekt:
C:\> cd (PyCharm : Project -> Copy Path/Reference -> Absolute Path)
4. Aktionen ausführen:
C:\> rasa run actions
5. Den Assistent in einem neuen Fenster ausführen:
C:\> rasa shell
6. Genießen Sie die Zeit mit Solik!

Beschreibung der entwickelten Dateien:

1. YAML-Dateien:
	- data/nlu.yml - enthält NLU-Trainingsdaten;
	- data/stories.yml - enthält Geschichten;
	- domain.yml - die Domänen Datei, einschließlich Bot-Antwortvorlagen.
2. Python-Dateien:
	- actions/actions.py: enthält benutzerdefinierten Aktionscode zum Finden von Räumen, Büros, Personen, Wetternachrichten
	- professors.py - Abrufen von Daten über Mitarbeitern von der Website: https://www.th-deg.de/de/hochschule/kontakt/fakultaet-ai
	- weather.py -Wetterdaten abrufen von der Webseite: https://openweathermap.org/api
3. JSON-Dateien:
	- offices.json - Liste der Büros auf dem Campus der THD;
	- persons.json - Liste der Mitarbeitern der Fakultät für Angewandte Informatik
4. models: 20211227-191944.tar.gz

Benötigte Versionen: Finden Sie die Benötigte Versionen von Python und Rasa in der Detei "requirements.txt"