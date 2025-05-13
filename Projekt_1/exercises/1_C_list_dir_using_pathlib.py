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

Skorzystaj z metody pathlib.Path(ścieżka).rglob('*') 
"""

import sys
import os
from pathlib import Path

# Domyślna ścieżka jeśli nie podano argumentu
DEFAULT_DIR = r"C:\Tomek\kursy_i_szkolenia\python\gynvael_python_10\Projekt_1\exercises"

# przejscie po drzewie katalogow i zebranie danych
def list_directory(path):
    """
    List the contents of a directory and its subdirectories using pathlib.
    Args:
        path (str): The path to the directory to list.
    Returns:
        list: List of file and directory names found.
    """
    files_found = []
    path_obj = Path(path)
    
    # rglob('*') will recursively find all files and directories
    for item in path_obj.rglob('*'):
        files_found.append(item.name)
    
    return files_found

def main():
    # Sprawdzenie argumentów wiersza poleceń
    if len(sys.argv) != 2:
        print(f"Nie podano ścieżki, używam domyślnej: {DEFAULT_DIR}")
        path = DEFAULT_DIR
    else:
        path = sys.argv[1]
        print(f"Path: {path}")
        
        # Sprawdzenie, czy ścieżka istnieje
        if not Path(path).exists():
            sys.exit(f"Błąd: Ścieżka '{path}' nie istnieje.")
    
    files_found = list_directory(path)
    
    # wyświetlenie danych w bardziej przyjazny sposób
    print(f"\nZnaleziono {len(files_found)} elementów:")
    for i, item in enumerate(files_found, 1):
        print(f"{i}. {item}")

if __name__ == "__main__":
    main()
