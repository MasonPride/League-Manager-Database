CREATE OR ALTER PROCEDURE League.FetchGame
   @GameID INT
AS

SELECT G.GameID, G.HomeTeamID, G.AwayTeamID, G.StadiumID, G.HomeScore, G.AwayScore, G.GameDate
FROM League.Games G
WHERE G.GameID = @GameID;
GO