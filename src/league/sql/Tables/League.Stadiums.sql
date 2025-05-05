IF OBJECT_ID(N'League.Stadiums') IS NULL
BEGIN
    CREATE TABLE League.Stadiums
    (
        StadiumID INT NOT NULL IDENTITY(1, 1),
        [Name] NVARCHAR(32) NOT NULL,
        Capacity INT NOT NULL,
        City NVARCHAR(32) NOT NULL,

        CONSTRAINT [PK_League_Stadiums_StadiumID] PRIMARY KEY CLUSTERED 
        (
            StadiumID ASC
        ),

        CONSTRAINT [UK_League_Stadiums_StadiumID] UNIQUE
        (
            [Name]
        )
    );
END;
