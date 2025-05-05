IF OBJECT_ID(N'League.TeamStats') IS NULL
BEGIN
    CREATE TABLE League.TeamStats
    (
        TeamStatID INT NOT NULL IDENTITY(1, 1),
        TeamID INT NOT NULL,
        Season INT NOT NULL,
        Wins INT NOT NULL,
        Losses INT NOT NULL,
        RunsScored INT NOT NULL,
        RunsAllowed INT NOT NULL,
        GamesPlayed INT NOT NULL,
        CONSTRAINT [PK_League_TeamStats_TeamStatID] PRIMARY KEY CLUSTERED 
        (
            TeamStatID ASC
        ),
        CONSTRAINT [FK_League_TeamStats_TeamID] FOREIGN KEY (TeamID) REFERENCES League.Teams(TeamID)
    );
END;