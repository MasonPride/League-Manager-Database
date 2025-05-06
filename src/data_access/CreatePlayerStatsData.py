import csv
import pyodbc

csv_path = 'src/league/Data/PlayerStats.csv'

conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=(local)\SQLEXPRESS;'
    r'DATABASE=DBEFinalProject;'
    r'Trusted_Connection=yes;'
    r'TrustServerCertificate=yes;'
)

cursor = conn.cursor()

with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("""
            EXEC League.SavePlayerStats 
                @PlayerID = ?, 
                @GamesPlayed = ?, 
                @Hits = ?, 
                @Runs = ?, 
                @HomeRuns = ?, 
                @RBI = ?
        """, int(row['PlayerID']), int(row['GamesPlayed']), int(row['Hits']),
             int(row['Runs']), int(row['HomeRuns']), int(row['RBI']))

conn.commit()
cursor.close()
conn.close()