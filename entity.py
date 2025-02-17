import json


class Entity(object):
    def __init__(self, x, y, identifier, color):
        self.x = x
        self.y = y
        self.identifier = identifier
        self.color = color

    def serialize(self):
        return json.dumps({
            "x": self.x,
            "y": self.y,
            "id": self.identifier,
            "red": self.color[0],
            "green": self.color[1],
            "blue": self.color[2],
        })

    @staticmethod
    def deserialize(serialized):
        d = json.loads(serialized)

        return Entity(
            d["x"],
            d["y"],
            d["id"],
            (d["red"],d["green"], d["blue"])
        )
