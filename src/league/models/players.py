class Players:
    def __init__(self, player_id: int, team_id: int, first_name: str, last_name: str, birthday: str, position: str, salary: float):
        self._player_id = person_id
        self._first_name = first_name
        self._last_name = last_name
        self._birthday = birthday
        self._position = position
        self._salary = salary

    @property
    def player_id(self):
        return self._player_id

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def birthday(self):
        return self._birthday

    @property
    def position(self):
        return self._position

    @property
    def salary(self):
        return self._salary
