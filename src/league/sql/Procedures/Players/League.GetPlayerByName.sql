CREATE OR ALTER PROCEDURE League.GetPlayerByName
   @FirstName NVARCHAR(32),
   @LastName NVARCHAR(32)
AS

SELECT P.PlayerID, P.TeamID, P.FirstName, P.LastName, P.Number, P.Birthday, P.Position
FROM League.Players P
WHERE LTRIM(RTRIM(P.FirstName)) = LTRIM(RTRIM(@FirstName))
  AND LTRIM(RTRIM(P.LastName)) = LTRIM(RTRIM(@LastName));
GO