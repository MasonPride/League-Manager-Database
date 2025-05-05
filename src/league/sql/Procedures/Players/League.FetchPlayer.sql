CREATE OR ALTER PROCEDURE League.FetchPlayer
   @PlayerID INT
AS

SELECT P.PlayerID, P.TeamID, P.FirstName, P.LastName, P.Number, P.Birthday, P.Postion
FROM League.Players P
WHERE P.PlayerID = @PlayerID;
GO