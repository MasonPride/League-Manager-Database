CREATE OR ALTER PROCEDURE League.FetchTeam
   @TeamID INT
AS

SELECT T.TeamID, T.StadiumID, T.Name, T.City, T.FoundedDay
FROM League.Teams T
WHERE T.TeamID = @TeamID;
GO