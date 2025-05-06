CREATE OR ALTER PROCEDURE League.SavePlayer
    @PlayerID INT,
    @TeamID INT,
    @FirstName NVARCHAR(32),
    @LastName NVARCHAR(32),
    @Number INT,
    @Birthday DATE,
    @Position NVARCHAR(32)
AS

MERGE League.Players AS T
USING (
    VALUES (@PlayerID, @TeamID, @FirstName, @LastName, @Number, @Birthday, @Position)
) AS S (PlayerID, TeamID, FirstName, LastName, [Number], Birthday, Position)
    ON T.PlayerID = S.PlayerID
WHEN MATCHED AND NOT EXISTS (
    SELECT S.TeamID, S.FirstName, S.LastName, S.Number, S.Birthday, S.Position
        INTERSECT
    SELECT T.TeamID, T.FirstName, T.LastName, T.Number, T.Birthday, T.Position
) THEN
    UPDATE SET
        T.TeamID = S.TeamID,
        T.FirstName = S.FirstName,
        T.LastName = S.LastName,
        T.Number = S.Number,
        T.Birthday = S.Birthday,
        T.Position = S.Position
WHEN NOT MATCHED BY TARGET THEN
    INSERT (TeamID, FirstName, LastName, [Number], Birthday, Position)
    VALUES (S.TeamID, S.FirstName, S.LastName, S.Number, S.Birthday, S.Position);
GO