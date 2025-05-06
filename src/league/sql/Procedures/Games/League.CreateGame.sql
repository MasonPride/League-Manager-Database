CREATE OR ALTER PROCEDURE League.CreateGame
   @HomeTeamID INT, 
   @AwayTeamID INT, 
   @StadiumID INT,
   @GameDate DATE,
   @GameID INT OUTPUT
AS

INSERT League.Games(HomeTeamID, AwayTeamID, StadiumID, GameDate)
VALUES(@HomeTeamID, @AwayTeamID, @StadiumID, @GameDate);

SET @GameID = SCOPE_IDENTITY();
GO
