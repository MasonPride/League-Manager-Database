IF OBJECT_ID(N'League.Games') IS NULL
BEGIN
    CREATE TABLE League.Games
    (
        GameID INT NOT NULL IDENTITY(1, 1),
        HomeTeamID INT NOT NULL,
        AwayTeamID INT NOT NULL,
        StadiumID INT NOT NULL,
        HomeScore INT NOT NULL DEFAULT 0,
        AwayScore INT NOT NULL DEFAULT 0,
        GameDate DATE NOT NULL,
        CONSTRAINT [PK_League_Games_GameID] PRIMARY KEY CLUSTERED 
        (
            GameID ASC
        ),
        CONSTRAINT [FK_League_Games_HomeTeamID] FOREIGN KEY (HomeTeamID) REFERENCES League.Teams(TeamID),
        CONSTRAINT [FK_League_Games_AwayTeamID] FOREIGN KEY (AwayTeamID) REFERENCES League.Teams(TeamID),
        CONSTRAINT [FK_League_Games_StadiumID] FOREIGN KEY (StadiumID) REFERENCES League.Stadiums(StadiumID)
    );
END;