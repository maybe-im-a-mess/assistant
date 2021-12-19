from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import json
from weather import say_weather


class Greeting(Action):
    def name(self) -> Text:
        return "say_hello"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_greet("Hello")

        return [AllSlotsReset()]


class Room(Action):
    def name(self) -> Text:
        return "action_find_room"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        room = tracker.get_slot("room")
        lst_room = []
        try:
            for i in room:
                lst_room.append(i)
            dispatcher.utter_message(template="utter_room", room=room, building=lst_room[0], floor=lst_room[1])
            return [AllSlotsReset()]
        except TypeError:
            dispatcher.utter_message(template="utter_help")
            return [AllSlotsReset()]


class Person(Action):
    def name(self) -> Text:
        return "action_find_person"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        person_to_find = tracker.get_slot("person")
        office = ""
        with open('persons.json', "r", encoding="UTF-8") as file:
            professors = json.load(file)
        try:
            for i in range(len(professors)):
                name = professors[i]["name"]
                if name.find(person_to_find) != -1:
                    office = professors[i]["room"]
            dispatcher.utter_message(template="utter_person", office=office)
            return [AllSlotsReset()]
        except TypeError:
            dispatcher.utter_message(template="utter_help")
            return [AllSlotsReset()]


class Office(Action):
    def name(self) -> Text:
        return "action_find_office"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        office_to_find = tracker.get_slot("office")
        location = ""
        with open('offices.json', "r", encoding="UTF-8") as file:
            offices = json.load(file)
        try:
            for i in range(len(offices)):
                office = offices[i]["office"]
                if office.find(office_to_find) != -1:
                    location = offices[i]["location"]
            dispatcher.utter_message(template="utter_office", office=office_to_find, location=location)
            return [AllSlotsReset()]

        except TypeError:
            dispatcher.utter_message(template="utter_help")
            return [AllSlotsReset()]


class Weather(Action):

    def name(self) -> Text:
        return "tell_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        actual_weather, temp = say_weather('deggendorf')
        dispatcher.utter_message(template="utter_temp", actual_weather=actual_weather, temp=temp)

        return [AllSlotsReset()]
