CREATE OR ALTER PROCEDURE League.GetStadiumByName
   @Name NVARCHAR(32)
AS

SELECT S.StadiumID, S.Name, S.Capacity, S.City
FROM League.Stadiums S
WHERE S.Name = @Name;
GO
