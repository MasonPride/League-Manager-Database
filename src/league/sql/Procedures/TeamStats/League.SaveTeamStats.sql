CREATE OR ALTER PROCEDURE League.SaveTeamStats
    @TeamID INT,
    @Wins INT,
    @Losses INT,
    @RunsScored INT,
    @RunsAllowed INT,
    @GamesPlayed INT
AS
BEGIN
    MERGE League.TeamStats AS T
    USING (SELECT @TeamID AS TeamID) AS S
        ON T.TeamID = S.TeamID
    WHEN MATCHED THEN
        UPDATE SET
            Wins = @Wins,
            Losses = @Losses,
            RunsScored = @RunsScored,
            RunsAllowed = @RunsAllowed,
            GamesPlayed = @GamesPlayed;
END;
GO