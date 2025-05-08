Param(
    [string] $Server = "(local)\SQLEXPRESS",
    [string] $Database = "DBEFinalProject",
    [string] $Dir = "src"
)

# This script requires the SQL Server module for PowerShell.

$CurrentDrive = (Get-Location).Drive.Name + ":"

Write-Host ""
Write-Host "Rebuilding database $Database on $Server..."

Write-Host "Dropping tables..."
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Tables\DropTables.sql" -TrustServerCertificate

Write-Host "Creating schema..."
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Schemas\League.sql" -TrustServerCertificate

Write-Host "Creating tables..."
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Tables\League.Stadiums.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Tables\League.Teams.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Tables\League.Players.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Tables\League.Games.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Tables\League.PlayerStats.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Tables\League.TeamStats.sql" -TrustServerCertificate

Write-Host "Stadiums Stored procedures..."
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Stadiums\League.FetchStadium.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Stadiums\League.GetStadiumByName.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Stadiums\League.GetAllStadiums.sql" -TrustServerCertificate

Write-Host "Games Stored procedures..."
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Games\League.FetchGame.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Games\League.CreateGame.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Games\League.SaveGame.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Games\League.GetAllGames.sql" -TrustServerCertificate

Write-Host "Teams Stored procedures..."
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Teams\League.FetchTeam.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Teams\League.GetTeamByName.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Teams\League.SaveTeam.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Teams\League.GetAllTeams.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Teams\League.GetAllPlayersOnTeam.sql" -TrustServerCertificate

Write-Host "Players Stored procedures..."
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Players\League.FetchPlayer.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Players\League.GetPlayerByName.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Players\League.CreatePlayer.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Players\League.SavePlayer.sql" -TrustServerCertificate

Write-Host "PlayerStats Stored procedures..."
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\PlayerStats\League.SavePlayerStats.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\PlayerStats\League.GetPlayerStats.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\PlayerStats\League.CreateStatsOnPlayerTrigger.sql" -TrustServerCertificate

Write-Host "TeamStats Stored procedures..."
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\TeamStats\League.SaveTeamStats.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\TeamStats\League.GetTeamStats.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\TeamStats\League.CreateStatsOnTeamTrigger.sql" -TrustServerCertificate

Write-Host "Aggregates Stored procedures..."
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Aggregates\League.GetAverageStatsByPosition.sql" -TrustServerCertificate

Write-Host "Inserting Data..."
python "$Dir\data_access\CreateStadiumsData.py"
python "$Dir\data_access\CreateTeamsData.py"
python "$Dir\data_access\CreatePlayersData.py"
python "$Dir\data_access\CreatePlayerStatsData.py"


Set-Location $CurrentDrive