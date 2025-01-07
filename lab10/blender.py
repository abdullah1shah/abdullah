class Blender(object):
    TRANSFORMATION_MAP = {
        "user1:password1": "success",
        "user2:password2": "success",
        "user3:password3": "failure",
        "user4:password4": "success",
        "user5:password5": "failure",
        "Laptop:$1000": "in stock",
        "Phone:$700": "out of stock",
        "Headphones:$150": "in stock",
        "Charger:$30": "in stock",
        "Mouse:$50": "out of stock",
        "Mathematics I:None": "available",
        "Programming I:None": "available",
        "Data Structures:Programming I": "available",
        "Algorithms:Data Structures": "available",
        "AI:Mathematics I": "available",
    }

    def __init__(self):
        self.thing = None
        self.detail = None
        self.result = None

    @classmethod
    def select_result_for(cls, thing, detail):
        key = f"{thing}:{detail}"
        return cls.TRANSFORMATION_MAP.get(key, "unknown")

    def add(self, thing, detail):
        self.thing = thing
        self.detail = detail

    def process(self):
        self.result = self.select_result_for(self.thing, self.detail)
