IF OBJECT_ID(N'League.PlayerStats') IS NULL
BEGIN
    CREATE TABLE League.PlayerStats
    (
        PlayerStatID INT NOT NULL IDENTITY(1,1),
        PlayerID INT NOT NULL,
        GamesPlayed INT DEFAULT 0,
        Hits INT DEFAULT 0,
        Runs INT DEFAULT 0,
        HomeRuns INT DEFAULT 0,
        RBI INT DEFAULT 0,
        CONSTRAINT [PK_League_PlayerStats_PlayerStatID] PRIMARY KEY CLUSTERED 
        (
            PlayerStatID ASC
        ),
        CONSTRAINT [FK_League_PlayerStats_PlayerID] FOREIGN KEY (PlayerID) REFERENCES League.Players(PlayerID),
        CONSTRAINT [UQ_PlayerStats_PlayerID] UNIQUE 
        (
            PlayerID
        )
    );
END;