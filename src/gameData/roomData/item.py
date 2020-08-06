class Item:
    def __init__(self, name, value, weight, size, desc, inspection):
        self.name = name
        self.value = value
        self.weight = weight
        self.size = size
        self.desc = desc
        self.inspection = inspection

class Tool(Item):
    def __init__(self, name, value, weight, size, desc, inspection, quality, multiplier = 1):
        self.quality = quality
        self.multiplier = multiplier
        super().__init__(name, value, weight, size, desc, inspection)

class Weapon(Item):
    def __init__(self, name, value, weight, size, desc, inspection, quality, damageRange, damageType, speed, multiplier = 1):
        self.quality = quality
        self.damageRange = damageRange
        self.damageType = damageType
        self.speed = speed
        self.multiplier = multiplier
        super().__init__(name, value, weight, size, desc, inspection)