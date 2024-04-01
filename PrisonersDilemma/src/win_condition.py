import random

class WinCondition:
    def __init__(self):
        self.name = self.__get_random_name()
        self.location = self.__get_random_location()
        self.item = self.__get_random_item()

    def __str__(self):
        return f"Name: {self.name}, Location: {self.location}, Item: {self.item}"

    def __repr__(self):
        return f"Name: {self.name}, Location: {self.location}, Item: {self.item}"
    
    def __dict__(self):
        return {
            "name": self.name,
            "location": self.location,
            "item": self.item
        }

    def __get_random_name(self):
        names = ["Fred", "George", "Harry", "Ron", "Hermione", "Draco", "Luna", "Neville", "Ginny", "Cho"]
        return names[random.randint(0, len(names)-1)]

    def __get_random_location(self):
        locations = ["kitchen", "bathroom", "bedroom", "attic", "basement", "backyard", "garage"]
        return locations[random.randint(0, len(locations)-1)]

    def __get_random_item(self):
        items = ["money", "jewelry", "art", "documents", "clothing"]
        return items[random.randint(0, len(items)-1)]