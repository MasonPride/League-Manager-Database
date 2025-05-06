CREATE OR ALTER TRIGGER League.CreateStatsOnPlayerInsert
    ON League.Players
AFTER INSERT
AS
BEGIN
    INSERT INTO League.PlayerStats (PlayerID)
    SELECT PlayerID
    FROM inserted
    WHERE NOT EXISTS (
        SELECT 1 FROM League.PlayerStats WHERE PlayerID = inserted.PlayerID
    );
END;
GO