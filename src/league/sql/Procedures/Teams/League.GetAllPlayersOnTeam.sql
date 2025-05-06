CREATE OR ALTER PROCEDURE League.GetAllPlayersOnTeam
    @TeamID INT
AS
BEGIN
    SELECT 
        T.TeamID,
        T.Name AS TeamName,
        P.PlayerID,
        P.FirstName,
        P.LastName,
        P.Number,
        P.Birthday,
        P.Position
    FROM League.Teams T
        INNER JOIN League.Players P ON T.TeamID = P.TeamID
    WHERE T.TeamID = @TeamID;
END;
GO