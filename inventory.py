class Inventory:
    def __init__(self, cost=0.0, description="", units=0):
        self._cost = cost
        self._description = description
        self._units = units

    def cost(self):
        return self._cost

    def description(self):
        return self._description

    def units(self):
        return self._units
    
    def cost(self, cost):
        self._cost = cost

    def description(self, description):
        self._description = description

    def units(self, units):
        self._units = units
