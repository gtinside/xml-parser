class Item:
    def __init__(self, id, name, description, details):
        self.id = id
        self.name = name
        self.description = description
        self.details = details

class Detail:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Complex:
    def __init__(self, nested):
        self.nested = nested

class Nested:
    def __init__(self, level, nested=[], value=None):
        self.level = level
        self.nested = nested
        self.value = value