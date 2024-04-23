import os
from datetime import datetime
import shutil


def working_dir():
    print(os.getcwd())
    new_dir = input("Inserisci la directory di lavoro ---> ")
    try:
        os.chdir(new_dir)
    except FileNotFoundError:
        print("Directory non valida!")
    except:
        print("Errore generico")
    print(os.getcwd())


def info_file():
    file_name = "d:\prova.txt"
    print(f"File size: {str(os.path.getsize(file_name))} bytes")

    created_at = datetime.fromtimestamp(os.path.getctime(file_name)).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    print(f"File created at: {created_at}")

    modified_at = datetime.fromtimestamp(os.path.getmtime(file_name)).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    print(f"File modified at: {modified_at}")

    stats_list = os.stat(file_name)
    print(stats_list)


def check_path():
    path = input("Inserisci il path ---> ")
    if not (path):
        print("Path vuoto!")
        return

    exist = os.path.exists(path)
    if not exist:
        print("Path non esistente!")
        return

    is_file = os.path.isfile(path)
    if not is_file:
        print("Il path è una directory")
    else:
        print("Il path è un file")


def copia_sposta_file():
    path = "/Users/mattia/dev/pastrocci"

    filename_from = "file1.txt"
    full_filename_from = os.path.join(path, filename_from)
    if os.path.exists(full_filename_from):
        os.remove(full_filename_from)

    with open(full_filename_from, "w") as writer:
        writer.write("Stringa prova 123")

    filename_to = "file2.txt"
    full_filename_to = os.path.join(path, filename_to)
    if os.path.exists(full_filename_to):
        os.remove(full_filename_to)

    shutil.copy(full_filename_from, full_filename_to)

    filename_to = "file3.txt"
    full_filename_to = os.path.join(path, filename_to)
    if os.path.exists(full_filename_to):
        os.remove(full_filename_to)
    shutil.move(full_filename_from, full_filename_to)


if __name__ == "__main__":
        scelta = input(
            """
    Ciao, quale metodo vuoi provare?
    1 - Working dir
    2 - Info file
    3 - Check path
    4 - Copia&Sposta file\n"""
    )
    match scelta:
        case "1":
            working_dir()
        case "2":
            info_file()
        case "3":
            check_path()
        case "4":
            copia_sposta_file()

