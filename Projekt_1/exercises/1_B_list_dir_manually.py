"""
Napisz program, który listuje zawartość wskazanego katalogu oraz wszystkich podkatalogów (i 
podkatalogów-podkatalogów też, aż do dna). 
Program powinien przyjmować ścieżkę do katalogu w pierwszym argumencie. Możesz w tym celu 
posłużyć się listą argumentów sys.argv, np.: 
import sys 
if len(sys.argv) != 2: 
sys.exit("usage: args.py <path>") 
path = sys.argv[1] 
print(f"Path: {path}")

Skorzystaj z metod manualnych (rekursywnych) przechodząc drzewo katalogów; kilka przydatnych funkcji: 
os.listdir(ścieżka) LUB glob.glob("ścieżka/*") 
os.path.isdir 
os.path.isfile 
"""

import sys
from pathlib import Path

DIR_TO_SCAN = r"C:\Tomek\kursy_i_szkolenia\python\gynvael_python_10\Projekt_1\exercises"

# przejscie po drzewie katalogow i zebranie danych
def list_directory(path):
    """
    Rekurencyjnie listuje zawartość katalogu i wszystkich jego podkatalogów.
    
    Args:
        path (str): Ścieżka do katalogu do przeszukania.
    
    Returns:
        list: Lista nazw znalezionych plików i katalogów.
    """
    import os
    
    files_found = []
    
    # Pobierz listę wszystkich elementów w bieżącym katalogu
    elements = os.listdir(path)
    
    for element in elements:
        # Utwórz pełną ścieżkę do elementu
        full_path = os.path.join(path, element)
        
        # Dodaj nazwę elementu do listy wyników
        files_found.append(element)
        
        # Jeśli element jest katalogiem, rekurencyjnie przejdź przez niego
        if os.path.isdir(full_path):
            # Rekurencyjne wywołanie funkcji dla podkatalogu
            subdir_path = os.path.join(path, element)
            # Rekurencyjnie przeszukaj podkatalog i dodaj znalezione elementy
            subdir_files = list_directory(subdir_path)
            # Opcjonalnie możesz dodać pełne ścieżki lub same nazwy z podkatalogów
            files_found.extend(subdir_files)
    
    return files_found

def main():
        
    files_found = list_directory(DIR_TO_SCAN)
    # wyświetlenie danych
    print(f'Files found {files_found}')

if __name__ == "__main__":
   main()
