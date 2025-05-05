IF OBJECT_ID(N'League.Players') IS NULL
BEGIN
    CREATE TABLE League.Players
    (
        PlayerID INT NOT NULL IDENTITY(1, 1),
        TeamID INT NOT NULL,
        FirstName NVARCHAR(32) NOT NULL,
        LastName NVARCHAR(32) NOT NULL,
        [Number] INT NOT NULL,
        Birthday DATE NOT NULL,
        Position NVARCHAR(32) NOT NULL,
        CONSTRAINT [PK_League_Players_PlayerID] PRIMARY KEY CLUSTERED 
        (
            PlayerID ASC
        ),
        CONSTRAINT [FK_League_Players_TeamID] FOREIGN KEY (TeamID) REFERENCES League.Teams(TeamID)
    );
END;