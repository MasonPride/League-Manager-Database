class Games:
    def __init__(self, game_id: int, home_team_id: int, away_team_id: int, stadium_id: int, game_date: str, home_score: int = 0, away_score: int = 0):
        self._game_id = game_id
        self._home_team_id = home_team_id
        self._away_team_id = away_team_id
        self._stadium_id = stadium_id
        self._home_score = home_score
        self._away_score = away_score
        self._game_date = game_date

    @property
    def game_id(self):
        return self._game_id

    @property
    def home_team_id(self):
        return self._home_team_id
    
    @property
    def away_team_id(self):
        return self._away_team_id

    @property
    def stadium_id(self):
        return self._stadium_id

    @property
    def home_score(self):
        return self._home_score
    
    @property
    def away_score(self):
        return self._away_score

    @property
    def game_date(self):
        return self._game_date
