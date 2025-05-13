"""
Zapoznaj się z tematyką wyrażeń regularnych (biblioteka re, funkcja re.match(...)). 
Zaproponuj po 3 różne wyrażenia regularne dla danego języka i zaimplementuj rozpoznawania 
języka programowania za ich pomocą. 
Hint: Najlepiej rozbij program na linie (metody readlines() albo splitlines() i testuj każdą linię 
osobno). 
Np. 
Python: 
"from.*import" 
"for.*in.*:" 
"""

import sys
import os
import re

FILE = r"C:\Tomek\kursy_i_szkolenia\python\gynvael_python_10\Projekt_1\exercises\flag_base64.py"
LANGUAGES = {
    "C/C++": [r"#include", r"#define"],
    "PHP": [r"<\?php"],
    "Python": [r"def ", r"import ", r"from.*import"],
    "HTML": [r"<html", r"<body", r"<div"]
}

def detect_language(file_path):
    detected_languages = set()
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
            for line in content:
                for language, patterns in LANGUAGES.items():
                    for pattern in patterns:
                        if re.search(pattern, line):
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
        print(f"No path provided, using default: {os.path.basename(file_path)}")
    else:
        file_path = sys.argv[1]
    
    # Check if the file is empty
    if is_file_empty(file_path):
        print(f"File is empty: {file_path}")
        return
    
    detected_languages = detect_language(file_path)
    
    # Display data in a user-friendly way
    print(f"\nDetected languages in '{os.path.basename(file_path)}':")
    for i, item in enumerate(detected_languages, 1):
        print(f"{i}. {item}")

if __name__ == "__main__":
    main()
    