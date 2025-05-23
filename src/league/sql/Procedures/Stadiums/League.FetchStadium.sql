CREATE OR ALTER PROCEDURE League.FetchStadium
   @StadiumID INT
AS

SELECT S.StadiumID, S.Name, S.Capacity, S.City
FROM League.Stadiums S
WHERE S.StadiumID = @StadiumID;
GO
