CREATE OR ALTER PROCEDURE League.SaveGame
    @GameID INT,
    @HomeTeamID INT,
    @AwayTeamID INT,
    @StadiumID INT,
    @HomeScore INT,
    @AwayScore INT,
    @GameDate DATE
AS

MERGE League.Games AS T
USING (
    VALUES (@GameID, @HomeTeamID, @AwayTeamID, @StadiumID, @HomeScore, @AwayScore, @GameDate)
) AS S (GameID, HomeTeamID, AwayTeamID, StadiumID, HomeScore, AwayScore, GameDate)
    ON T.GameID = S.GameID
WHEN MATCHED AND NOT EXISTS (
    SELECT S.HomeTeamID, S.AwayTeamID, S.StadiumID, S.HomeScore, S.AwayScore, S.GameDate
    INTERSECT
    SELECT T.HomeTeamID, T.AwayTeamID, T.StadiumID, T.HomeScore, T.AwayScore, T.GameDate
) THEN
    UPDATE SET
        T.HomeTeamID = S.HomeTeamID,
        T.AwayTeamID = S.AwayTeamID,
        T.StadiumID = S.StadiumID,
        T.HomeScore = S.HomeScore,
        T.AwayScore = S.AwayScore,
        T.GameDate = S.GameDate
WHEN NOT MATCHED BY TARGET THEN
    INSERT (HomeTeamID, AwayTeamID, StadiumID, HomeScore, AwayScore, GameDate)
    VALUES (S.HomeTeamID, S.AwayTeamID, S.StadiumID, S.HomeScore, S.AwayScore, S.GameDate);
GO
