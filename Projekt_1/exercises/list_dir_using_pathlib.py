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

===== ZROBIONE =====

"""

import sys
from pathlib import Path

DIR_TO_SCAN = r"C:\Tomek\kursy_i_szkolenia\python\gynvael_python_10\Projekt_1\exercises"

# przejscie po drzewie katalogow i zebranie danych
def list_directory(path):
    """
    List the contents of a directory and its subdirectories using pathlib.
    Args:
        path (str): The path to the directory to list.
    """
    files_found = []
    path_obj = Path(path)
    
    # rglob('*') will recursively find all files and directories
    for item in path_obj.rglob('*'):
        files_found.append(item.name)
    
    return files_found

def main():
        
    files_found = list_directory(DIR_TO_SCAN)
    # wyświetlenie danych
    print(f'Files found {files_found}')

if __name__ == "__main__":
   main()
