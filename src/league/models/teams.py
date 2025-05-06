class Teams:
    def __init__(self, team_id, stadium_id: int, name: str, city: str, founded_day: str):
        self._team_id = team_id
        self._stadium_id = stadium_id
        self._name = name
        self._city = city
        self._founded_day = founded_day

    @property
    def team_id(self):
        return self._team_id

    @property
    def stadium_id(self):
        return self._stadium_id

    @property
    def name(self):
        return self._name

    @property
    def city(self):
        return self._city
    
    @property
    def founded_day(self):
        return self._founded_day
