# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

import requests
import json


# x = requests.get('')
# print(x.text)


class Greeting(Action):
    def name(self) -> Text:
        return "say_hello"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_greet("Hello")

        return []


class Room(Action):
    def name(self) -> Text:
        return "action_find_room"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        room = tracker.get_slot("room")
        lst_room = []
        for i in room:
            lst_room.append(i)
        dispatcher.utter_attachment("Raum {} befindet sich im Gebäude {} auf der {} Etage".format(room, lst_room[0], lst_room[1]))

        return [SlotSet("room", room)]


class Person(Action):
    def name(self) -> Text:
        return "action_find_person"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        person_to_find = tracker.get_slot("person")
        with open('persons.json', "r", encoding="UTF-8") as file:
            professors = json.load(file)
        for i in range(len(professors)):
            name = professors[i]["name"]
            if name.find(person_to_find) != -1:
                office = professors[i]["room"]
        dispatcher.utter_attachment("Versuch mal das Zimmer {}".format(office))

        return [SlotSet("person", person_to_find)]


