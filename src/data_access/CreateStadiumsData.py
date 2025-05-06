import csv
import pyodbc

csv_path = 'src/league/Data/Stadiums.csv'

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
            INSERT INTO League.Stadiums (Name, Capacity, City)
            VALUES (?, ?, ?)
        """, row['Name'], int(row['Capacity']), row['City'])

conn.commit()
cursor.close()
conn.close()