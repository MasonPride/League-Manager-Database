CREATE OR ALTER PROCEDURE League.GetTeamByName
   @Name NVARCHAR(128)
AS

SELECT T.TeamID, T.StadiumID, T.Name, T.City, T.FoundedDay
FROM League.Teams T
WHERE T.Name = @Name;
GO