"""Bęzie to najprostszy program, ktory zlicza linie w pliku tekstowym."""

import sys
import os

FILE = r"C:\Tomek\kursy_i_szkolenia\python\gynvael_python_10\Projekt_1\exercises\flag_base64.py"

def count_lines_in_file(file_path):
    """
    Zlicza linie w pliku tekstowym, pomijając:
    - puste linie
    - linie zawierające tylko komentarz jednoliniowy
    
    Args:
        file_path (str): Ścieżka do pliku tekstowego.
    
    Returns:
        int: Liczba niepustych, niekomentarzowych linii w pliku.
    """
    try:
        with open(file_path, 'r') as file:
            # Zliczanie tylko niepustych linii, które nie są tylko komentarzami
            lines = [line for line in file.readlines() 
                    if line.strip() and not line.strip().startswith('#')]
            return len(lines)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return 0

def main():
    # Sprawdzenie liczby argumentów
    if len(sys.argv) != 2:
        # Jeśli nie podano argumentu, użyj domyślnego pliku
        file_path = FILE
        print(f"Nie podano ścieżki do pliku, używam domyślnej: {os.path.basename(file_path)}")
    else:
        file_path = sys.argv[1]
    
    # Zliczanie linii w pliku
    line_count = count_lines_in_file(file_path)
    
    # Wyświetlenie wyniku - tylko nazwa pliku zamiast pełnej ścieżki
    file_name = os.path.basename(file_path)
    print(f"Liczba linii w pliku '{file_name}': {line_count}")

if __name__ == "__main__":
    main()
