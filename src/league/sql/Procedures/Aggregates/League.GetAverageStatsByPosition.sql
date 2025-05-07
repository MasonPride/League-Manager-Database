CREATE OR ALTER PROCEDURE League.GetAverageStatsByPosition
AS
BEGIN
    SELECT P.Position, AVG(S.Runs) AS AvgRuns, AVG(S.HomeRuns) AS AvgHomeRuns, AVG(S.Strikeouts) AS AvgStrikeouts
    FROM League.PlayerStats S
    INNER JOIN League.Players P ON S.PlayerID = P.PlayerID
    GROUP BY P.Position
    ORDER BY P.Position;
END;