import csv
import pyodbc

csv_path = 'src/league/Data/Teams.csv'

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
            INSERT INTO League.Teams (StadiumID, Name, City, FoundedDay)
            VALUES (?, ?, ?, ?)
        """, int(row['StadiumID']), row['Name'], row['City'], row['FoundedDay'],)

conn.commit()
cursor.close()
conn.close()