Param(
    [string] $Server = "(local)\SQLEXPRESS",
    [string] $Database = "DBEFinalProject",
    [string] $Dir = "src"
)

# This script requires the SQL Server module for PowerShell.
# The below commands may be required.

# To check whether the module is installed.
# Get-Module -ListAvailable -Name SqlServer;

# Install the SQL Server Module
# Install-Module -Name SqlServer -Scope CurrentUser

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

Write-Host "Stadium Stored procedures..."
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Stadiums\League.FetchStadium.sql" -TrustServerCertificate
Invoke-SqlCmd -ServerInstance $Server -Database $Database -InputFile "$Dir\league\sql\Procedures\Stadiums\League.GetStadiumByName.sql" -TrustServerCertificate


Write-Host "Inserting Data..."
python "$Dir\data_access\CreateStadiumsData.py"
python "$Dir\data_access\CreateTeamsData.py"


Set-Location $CurrentDrive