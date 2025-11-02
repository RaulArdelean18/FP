# am adaugat sys si os ca sa pot avea in acelasi folder toate proiectele de la FP
import sys
import os

# Obtine calea absoluta a folderului in care se afla main.py
director_curent = os.path.dirname(os.path.abspath(__file__))
# Adauga aceasta cale in sys.path pentru ca Python sa gaseasca modulele (app, ui, etc.)
sys.path.append(director_curent)

from app.controller import *

if __name__ == "__main__":
    run()