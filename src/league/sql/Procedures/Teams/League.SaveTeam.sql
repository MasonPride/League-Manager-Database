CREATE OR ALTER PROCEDURE League.SaveTeam
    @TeamID INT,
    @StadiumID INT,
    @Name NVARCHAR(32),
    @City NVARCHAR(32),
    @FoundedDay DATE
AS

MERGE League.Teams AS T
USING (
    VALUES (@TeamID, @StadiumID, @Name, @City, @FoundedDay)
) AS S (TeamID, StadiumID, [Name], City, FoundedDay)
    ON T.TeamID = S.TeamID
WHEN MATCHED AND NOT EXISTS (
    SELECT S.StadiumID, S.Name, S.City, S.FoundedDay
    INTERSECT
    SELECT T.StadiumID, T.Name, T.City, T.FoundedDay
) THEN
    UPDATE SET
        T.StadiumID = S.StadiumID,
        T.Name = S.Name,
        T.City = S.City,
        T.FoundedDay = S.FoundedDay;
GO