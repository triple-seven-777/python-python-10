""" 
Program powinien wczytywać (tekstowo) zawartość pliku, a następnie sprawdzać czy 
występują we wczytanym stringu (operator in) znajdują się poniższe słowa kluczowe 
(pogrupowane dla danego języka): 

C/C++: 
"#include" 
"#define" 

PHP: 
"<?php" 

Python: 
"def " 
"import " 

HTML: 
"<html" 
"<body" 
"<div" 

Jeśli któryś string zostanie znaleziony, wypisz nazwę znalezionego języka i kontynuuj 
poszukiwania dalej. Nazwę konkretnego języka wypisz tylko raz (można to osiągnąć na wiele 
sposób). 
"""

import sys
import os

FILE = r"C:\Tomek\kursy_i_szkolenia\python\gynvael_python_10\Projekt_1\exercises\flag_base64.py"

LANGUAGES = {
    "C/C++": ["#include", "#define"],
    "PHP": ["<?php"],
    "Python": ["def ", "import "],
    "HTML": ["<html", "<body", "<div"]
}

def detect_language_guess_lexer(file_path):
    try:
        from pygments.lexers import guess_lexer
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        lexer = guess_lexer(content)
        return lexer.name
    except Exception:
        return None

def detect_language(file_path):
    detected_languages = set()
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            for language, keywords in LANGUAGES.items():
                for keyword in keywords:
                    if keyword in content:
                        detected_languages.add(language)
                        break
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    return list(detected_languages)

def is_file_empty(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readable() and file.read().strip() == ""
    except Exception as e:
        print(f"File is empty {file_path}: {e}")
        return True
    
def main():
    if len(sys.argv) != 2:
        file_path = FILE
        print(f"Nie podano ścieżki do pliku, używam domyślnej: {os.path.basename(file_path)}")
    else:
        file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"Plik '{file_path}' nie istnieje.")
        return
    if is_file_empty(file_path):
        print(f"Plik '{file_path}' jest pusty.")
        return

    lexer_name = detect_language_guess_lexer(file_path)
    if lexer_name:
        print(f"(pygments) Zgadnięty język: {lexer_name}")

    detected_languages = detect_language(file_path)
    if detected_languages:
        print(f"Wykryte języki w pliku '{os.path.basename(file_path)}': {', '.join(detected_languages)}")
    else:
        print(f"Nie wykryto żadnego języka w pliku '{os.path.basename(file_path)}'.")

if __name__ == "__main__":
    main()
