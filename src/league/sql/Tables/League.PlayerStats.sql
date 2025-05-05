IF OBJECT_ID(N'League.PlayerStats') IS NULL
BEGIN
    CREATE TABLE League.PlayerStats
    (
        PlayerStatID INT NOT NULL IDENTITY(1, 1),
        PlayerID INT NOT NULL,
        GameID INT NOT NULL,
        Hits INT NOT NULL,
        AtBats INT NOT NULL,
        RBI INT NOT NULL,
        Strikeouts INT NOT NULL,
        Walks INT NOT NULL,
        HitByPitch INT NOT NULL,
        Homeruns INT NOT NULL,
        CONSTRAINT [PK_League_PlayerStats_PlayerStatID] PRIMARY KEY CLUSTERED 
        (
            PlayerStatID ASC
        ),
        CONSTRAINT [FK_League_PlayerStats_PlayerID] FOREIGN KEY (PlayerID) REFERENCES League.Players(PlayerID),
        CONSTRAINT [FK_League_PlayerStats_GameID] FOREIGN KEY (GameID) REFERENCES League.Games(GameID)
    );
END;