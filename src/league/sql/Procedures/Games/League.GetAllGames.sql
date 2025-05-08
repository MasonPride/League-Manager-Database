CREATE OR ALTER PROCEDURE League.GetAllGames
AS
BEGIN
    SELECT 
        G.GameID,
        G.GameDate,
        G.HomeScore,
        G.AwayScore,
        HT.TeamID AS HomeTeamID,
        HT.Name AS HomeTeamName,
        AT.TeamID AS AwayTeamID,
        AT.Name AS AwayTeamName,
        S.StadiumID,
        S.Name AS StadiumName
    FROM League.Games G
    INNER JOIN League.Teams HT ON G.HomeTeamID = HT.TeamID
    INNER JOIN League.Teams AT ON G.AwayTeamID = AT.TeamID
    INNER JOIN League.Stadiums S ON G.StadiumID = S.StadiumID
    ORDER BY G.GameDate ASC;
END;
GO
