import sys
import os
import subprocess

def create_venv_and_install_pygments(venv_path):
    try:
        subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)
        subprocess.run([os.path.join(venv_path, "Scripts", "pip"), "install", "pygments"], check=True)
        print("Środowisko wirtualne utworzone i biblioteka 'pygments' zainstalowana.")
    except Exception as e:
        print(f"Błąd podczas tworzenia środowiska wirtualnego lub instalacji biblioteki: {e}")
        sys.exit(1)

def detect_language_with_pygments(file_path, venv_path):
    # Import pygments after venv is activated
    sys.path.insert(0, os.path.join(venv_path, "Lib", "site-packages"))
    try:
        from pygments.lexers import guess_lexer
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        lexer = guess_lexer(content)
        print(f"Zgadnięty język: {lexer.name}")
    except Exception as e:
        print(f"Błąd podczas rozpoznawania języka: {e}")
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Użycie: python 4_C_venv_intro.py <ścieżka_do_venv> <ścieżka_do_pliku>")
        sys.exit(1)
    venv_path = sys.argv[1]
    file_path = sys.argv[2]
    if not os.path.exists(file_path):
        print(f"Plik {file_path} nie istnieje.")
        sys.exit(1)

    create_venv_and_install_pygments(venv_path)
    detect_language_with_pygments(file_path, venv_path)

