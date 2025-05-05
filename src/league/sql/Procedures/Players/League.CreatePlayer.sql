CREATE OR ALTER PROCEDURE League.CreatePlayer
   @TeamID INT, 
   @FirstName NVARCHAR(32),
   @LastName NVARCHAR(32),
   @Number INT,
   @Birthday DATE,
   @Position NVARCHAR(32),
   @PlayerID INT OUTPUT
AS

INSERT League.Players(TeamID, FirstName, LastName, [Number], Birthday, Position)
VALUES(@TeamID, @FirstName, @LastName, @Number, @Birthday, @Position);

SET @PlayerID = SCOPE_IDENTITY();
GO
