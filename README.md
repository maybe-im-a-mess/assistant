<h1><b>Campus Navigation “Solik”</b></h1>

<b>Kurzbeschreibung:</b> 
Das System hilft bei der Suche nach allen Büros und Räumlichkeiten des Campus der THD sowie bei der Suche nach Professoren für die Fakultät für Angewandte Informatik und  informiert über das aktuelle Wetter in Deggendorf.

<b>Installationsbeschreibung:</b>
<ol>
<li>Rasa installieren:</li>
<ul>
  <li>Erstellen Sie eine neue virtuelle Umgebung, indem Sie einen Python-Interpreter auswählen und ein .\\venv-Verzeichnis erstellen, um es zu speichern. 
      Befehl für Windows: 
      <code>C:\> python3 -m venv ./venv</code></li>
  <li>Aktivieren Sie die virtuelle Umgebung. 
    <code>C:\> .\venv\Scripts\activate</code></li>
  <li>Installieren Sie Rasa Open Source mit pip (erfordert Python 3.7 oder 3.8). 
    <code>C:\> pip3 install -U --user pip && pip3 install rasa</code></li>
</ul>
<li>Das Projekt klonen:</li>
  https://github.com/maybe-im-a-mess/assistant.git
<li>Betreten Sie den Ordner mit dem Projekt:</li>
  <code>C:\> cd (PyCharm : Project -> Copy Path/Reference -> Absolute Path)</code>
<li>Aktionen ausführen:</li>
  <code>C:\> rasa run actions</code>
<li>Den Assistent in einem neuen Fenster ausführen:</li>
  <code>C:\> rasa shell</code>
<li>Genießen Sie die Zeit mit Solik!</li>
</ol>

<b>Beschreibung der entwickelten Dateien:</b>
<ul>
<li>YAML-Dateien:</li>
<ul>
<li>data/nlu.yml - enthält NLU-Trainingsdaten;</li>
<li>data/stories.yml - enthält Geschichten;</li>
<li>domain.yml - die Domänen Datei, einschließlich Bot-Antwortvorlagen.</li>
</ul>
<li>Python-Dateien:</li>
<ul>
<li>actions/actions.py: enthält benutzerdefinierten Aktionscode zum Finden von Räumen, Büros, Personen, Wetternachrichten</li>
<li>professors.py - Abrufen von Daten über Mitarbeitern von der Website:  https://www.th-deg.de/de/hochschule/kontakt/fakultaet-ai</li>
<li>weather.py -Wetterdaten abrufen von der Webseite: https://openweathermap.org/api</li>
</ul>
<li>JSON-Dateien:</li>
<ul>
<li>offices.json - Liste der Büros auf dem Campus der THD;</li>
<li>persons.json - Liste der Mitarbeitern der Fakultät für Angewandte Informatik</li>
</ul>
<li>models: 20211227-191944.tar.gz</li>
</ul>

<b>Benötigte Versionen:</b>
Finden Sie die Benötigte Versionen von Python und Rasa in der Detei <code>"requirements.txt"</code>
