CREATE OR ALTER PROCEDURE League.GetAllStadiums
AS
BEGIN
    SELECT 
        S.StadiumID,
        S.Name,
        S.Capacity,
        S.City
    FROM League.Stadiums S
    ORDER BY Name ASC;
END;
GO