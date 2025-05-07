class TeamStats:
    
    def __init__(self, team_stat_id: int, team_id: int, wins: int, losses: int, runs_scored: int, runs_allowed: int, games_played: int):
        self._team_stat_id = team_stat_id
        self._team_id = team_id
        self._wins = wins
        self._losses = losses
        self._runs_scored = runs_scored
        self._runs_allowed = runs_allowed
        self._games_played = games_played

    @property
    def team_stat_id(self):
        return self._team_stat_id

    @property
    def team_id(self):
        return self._team_id

    @property
    def wins(self):
        return self._wins

    @property
    def losses(self):
        return self._losses

    @property
    def runs_scored(self):
        return self._runs_scored

    @property
    def runs_allowed(self):
        return self._runs_allowed

    @property
    def games_played(self):
        return self._games_played
