import csv
import pyodbc

csv_path = 'src/league/Data/Players.csv'

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
        try:
            cursor.execute("""
                INSERT INTO League.Players (TeamID, FirstName, LastName, Number, Birthday, Position)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
            int(row['TeamID']),
            row['FirstName'],
            row['LastName'],
            int(row['Number']),
            row['Birthday'],
            row['Position']
            )
        except Exception as e:
            print(f"Failed to insert PlayerID {row['PlayerID']}: {e}")

conn.commit()
cursor.close()
conn.close()