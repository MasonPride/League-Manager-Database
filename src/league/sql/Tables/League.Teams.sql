IF OBJECT_ID(N'League.Teams') IS NULL
BEGIN
    CREATE TABLE League.Teams
    (
        TeamID INT NOT NULL IDENTITY(1, 1),
        StadiumID INT NOT NULL,
        [Name] NVARCHAR(32) NOT NULL,
        City NVARCHAR(32) NOT NULL,
        FoundedDay DATE NOT NULL,
        CONSTRAINT [PK_League_Teams_TeamID] PRIMARY KEY CLUSTERED 
        (
            TeamID ASC
        ),
        CONSTRAINT [FK_League_Teams_StadiumID] FOREIGN KEY (StadiumID) REFERENCES League.Stadiums(StadiumID)
    );
END;