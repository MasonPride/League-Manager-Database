CREATE OR ALTER TRIGGER League.CreateStatsOnTeamInsert
    ON League.Teams
AFTER INSERT
AS
BEGIN
    INSERT INTO League.TeamStats (TeamID)
    SELECT TeamID
    FROM inserted
    WHERE NOT EXISTS (
        SELECT 1 FROM League.TeamStats WHERE TeamID = inserted.TeamID
    );
END;
GO