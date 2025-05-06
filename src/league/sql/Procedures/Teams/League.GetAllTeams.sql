CREATE OR ALTER PROCEDURE League.GetAllTeams
AS

SELECT T.TeamID, T.StadiumID, T.Name, T.City, T.FoundedDay
FROM League.Teams T
GO
