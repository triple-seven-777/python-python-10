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

Skorzystaj z os.walk()

===== ZROBIONE =====

mozliwe iteracje:
- pytanie o katalog (bezposrednio w konsoli lub innym sposobem(?))
- podzial plikow na katalogi i pliki
- zliczanie plikow i katalogow
- zliczanie plikow i katalogow w danym katalogu

"""



import sys
import os

# wskazanie katalogu
DIR_TO_SCAN = r"C:\Tomek\kursy_i_szkolenia\python\gynvael_python_10\Projekt_1\exercises"


# przejscie po drzewie katalogow i zebranie danych
def list_directory(path=DIR_TO_SCAN):
    """
    List the contents of a directory and its subdirectories.
    Args:
        path (str): The path to the directory to list.
    """
    files_found = []
    for root, dirs, files in os.walk(path):
        for name in dirs:
           files_found.append(name)
        for name in files:
            files_found.append(name) 
    return files_found


def main():
    files_found = list_directory(DIR_TO_SCAN)
    # wyświetlenie danych
    print(f'Files found {files_found}')


if __name__ == "__main__":
   main()
