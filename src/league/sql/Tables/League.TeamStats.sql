IF OBJECT_ID(N'League.TeamStats') IS NULL
BEGIN
    CREATE TABLE League.TeamStats
    (
        TeamStatID INT NOT NULL IDENTITY(1, 1),
        TeamID INT NOT NULL,
        Wins INT DEFAULT 0,
        Losses INT DEFAULT 0,
        RunsScored INT DEFAULT 0,
        RunsAllowed INT DEFAULT 0,
        GamesPlayed INT DEFAULT 0,
        CONSTRAINT [PK_League_TeamStats_TeamStatID] PRIMARY KEY CLUSTERED 
        (
            TeamStatID ASC
        ),
        CONSTRAINT [FK_League_TeamStats_TeamID] FOREIGN KEY (TeamID) REFERENCES League.Teams(TeamID)
    );
END;