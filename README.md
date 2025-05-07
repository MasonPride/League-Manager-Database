# League Manager Database Project

This project is a relational database system designed for managing a sports league. It includes a full SQL schema, scripts to manage database lifecycle, and supporting Python scripts.

## Project Requirements

Before running the project, ensure you have the following installed:

- **ODBC Driver for SQL Server**  
  You will need to have the ODBC driver for SQL Server installed. You can download it from:  
  [Download ODBC Driver](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15)

- **Python Requirements**  
  Install all the required modules and packages:

  ```bash
  pip install -r requirements.txt

  ```

- **Powershell SQL Server Module**  
   The Powershell script requires the SQL Server moduel for Powershell.

  To check whether the module is installed:

  ```powershell
  Get-Module -ListAvailable -Name SqlServer
  ```

  To install the SQL Server Module:

  ```powershell
  Install-Module -Name SqlServer -AllowClobber
  ```

## How to Use

1. **Rebuild the Database**  
   Run the PowerShell script to drop and recreate tables:

   ```powershell
   ./RebuildDatabase-local.ps1

   ```

2. **Enviornment Variables**  
   Creat a `.env` file in the root of the project directory, and populate the env variables with the correct parameters. An env.sample file is given.

3. **Flask Server**
   To run the Flask server

   ```bash
   python -m flask run
   ```
