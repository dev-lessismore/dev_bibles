import os
from datetime import datetime

def working_dir():
    print(os.getcwd())
    new_dir = input('Inserisci la directory di lavoro ---> ')
    try:
        os.chdir(new_dir)
    except FileNotFoundError:
        print('Directory non valida!')
    except:
        print('Errore generico')
    print(os.getcwd())

def info_file():
    file_name = "d:\prova.txt"
    print(f"File size: {str(os.path.getsize(file_name))} bytes")

    created_at = datetime.fromtimestamp(os.path.getctime(file_name)).strftime('%Y-%m-%d %H:%M:%S')
    print(f"File created at: {created_at}")

    modified_at = datetime.fromtimestamp(os.path.getmtime(file_name)).strftime('%Y-%m-%d %H:%M:%S')
    print(f"File modified at: {modified_at}")

    stats_list = os.stat(file_name)
    print(stats_list)


def check_path():
    path = input
def copia_file():
    pass
def cancella_file():
    pass

    



if __name__ == "__main__":
    scelta = input('''
Ciao, quale metodo vuoi provare? 
1 - Working dir
2 - Info file
3 - Check path
4 - Cancella file\n''')
    match scelta:
        case "1":
            working_dir()
        case "2":
            info_file()
        case "3":
            check_path()
        case "4":
            cancella_file()
        case "5":
            copia_file()