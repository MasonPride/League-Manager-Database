CREATE OR ALTER PROCEDURE League.GetPlayerStats
    @PlayerID INT
AS
BEGIN
    SELECT 
        PS.PlayerStatID,
        PS.PlayerID,
        P.FirstName,
        P.LastName,
        PS.GamesPlayed,
        PS.Hits,
        PS.Runs,
        PS.HomeRuns,
        PS.RBI,
        PS.Strikeouts
    FROM League.PlayerStats PS
    JOIN League.Players P ON PS.PlayerID = P.PlayerID
    WHERE PS.PlayerID = @PlayerID;
END;
GO