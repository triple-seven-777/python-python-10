""" 
Zrób kopię programu z ćwiczenia 1 (dowolnego wariantu) i przerób go tak, aby zamiast wypisywać
wszystkie pliki i katalogi, wypisywał tylko unikatowe rozszerzenia plików.
Np. dla zawartości katalogów:
code.py
moarcode.py
website.html
podkatalog/
2025 © HexArcana Cybersecurity GmbH
Praktyczny Python
Projekt 1
(wersja: Maj-Lipiec'25)
podkatalog/asdf.txt
program powinien wypisać (w dowolnej kolejności):
.py
.html
.txt
Jeśli zobaczysz jakieś nieznane Ci rozszerzenia, ustal co to.
Przydatne funkcje:
os.path.splitext(...)
set() (struktura danych, jak lista, tylko bez duplikatów, i nie zachowuje kolejności)
set().add(...)
"""

import sys
import os
from pathlib import Path

# Default path if no argument is provided
DEFAULT_DIR = r"C:\Tomek\kursy_i_szkolenia\python\gynvael_python_10\Projekt_1\exercises"

# Traverse the directory tree and collect data
def list_directory(path):
    unique_ext_found = set()
    path_obj = Path(path)
    
    for item in path_obj.rglob('*'):
        if item.is_file():
            # Get file extension
            ext = item.suffix
            # Add extension to the set
            if ext:
                unique_ext_found.add(ext)
    
    return unique_ext_found

def main():
    # Check command line arguments
    if len(sys.argv) != 2:
        print(f"No path provided, using default: {DEFAULT_DIR}")
        path = DEFAULT_DIR
    else:
        path = sys.argv[1]
        print(f"Path: {path}")
        
        # Check if path exists
        if not Path(path).exists():
            sys.exit(f"Error: Path '{path}' does not exist.")
    
    unique_ext_found = list_directory(path)
    
    # Display data in a user-friendly way
    print(f"\nFound {len(unique_ext_found)} unique extensions:")
    for i, item in enumerate(unique_ext_found, 1):
        print(f"{i}. {item}")

if __name__ == "__main__":
    main()
