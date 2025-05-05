CREATE OR ALTER PROCEDURE League.GetPlayerByName
   @FirstName NVARCHAR(32)
   @LastName NVARCHAR(32)
AS

SELECT T.TeamID, T.StadiumID, T.Name, T.City, T.FoundedDay
FROM League.Teams T
WHERE T.FirstName = @FirstName
    AND T.LastName = @LastName;
GO