CREATE OR ALTER PROCEDURE League.GetTeamStats
    @TeamID INT
AS
BEGIN
    SELECT 
        TS.TeamStatID,
        TS.TeamID,
        TS.Wins,
        TS.Losses,
        TS.RunsScored,
        TS.RunsAllowed,
        TS.GamesPlayed
    FROM League.TeamStats TS
    WHERE TS.TeamID = @TeamID;
END;
GO