class PlayerStats:
    def __init__(self, player_stat_id: int, player_id: int, games_played: int, hits: int, runs: int, home_runs: int, rbi: int, strikeouts: int):
        self._player_stat_id = player_stat_id
        self._player_id = player_id
        self._games_played = games_played
        self._hits = hits
        self._runs = runs
        self._home_runs = home_runs
        self._rbi = rbi
        self._strikeouts = strikeouts

    @property
    def player_stat_id(self):
        return self._player_stat_id

    @property
    def player_id(self):
        return self._player_id

    @property
    def games_played(self):
        return self._games_played

    @property
    def hits(self):
        return self._hits

    @property
    def runs(self):
        return self._runs

    @property
    def home_runs(self):
        return self._home_runs

    @property
    def rbi(self):
        return self._rbi

    @property
    def strikeouts(self):
        return self._strikeouts
