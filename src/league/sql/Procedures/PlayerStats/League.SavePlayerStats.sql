CREATE OR ALTER PROCEDURE League.SavePlayerStats
    @PlayerID INT,
    @GamesPlayed INT,
    @Hits INT,
    @Runs INT,
    @HomeRuns INT,
    @RBI INT,
    @Strikeouts INT
AS
BEGIN
    MERGE League.PlayerStats AS T
    USING (SELECT @PlayerID AS PlayerID) AS S
        ON T.PlayerID = S.PlayerID
    WHEN MATCHED THEN
        UPDATE SET
            GamesPlayed = @GamesPlayed,
            Hits = @Hits,
            Runs = @Runs,
            HomeRuns = @HomeRuns,
            RBI = @RBI,
            Strikeouts = @Strikeouts
    WHEN NOT MATCHED THEN
        INSERT (PlayerID, GamesPlayed, Hits, Runs, HomeRuns, RBI, Strikeouts)
        VALUES (@PlayerID, @GamesPlayed, @Hits, @Runs, @HomeRuns, @RBI, @Strikeouts);
END;
GO