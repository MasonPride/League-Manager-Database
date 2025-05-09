"""Sample Main Project File.

Usage:
    python3 -m src - execute this program (when run from project root).

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""
import sys
from src.league.Main import Main
from src.league.Web import Web
print("In /src/__main__.py")
Main.main(sys.argv)
app = Web.main(sys.argv)
app.run()
