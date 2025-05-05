class Stadiums:
    def __init__(self, stadium_id: int, name: str, capacity: int, city: str):
        self._stadium_id = stadium_id
        self._name = name
        self._capacity = capacity
        self._city = city

    @property
    def stadium_id(self):
        return self._stadium_id

    @property
    def name(self):
        return self._name

    @property
    def capacity(self):
        return self._capacity

    @property
    def city(self):
        return self._city
