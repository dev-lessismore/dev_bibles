import os, zipfile, shutil


def crea_zip():
    path = "d:\\"
    zip_filename = os.path.join(path, "prova.zip")
    if os.path.exists(zip_filename):
        os.remove(zip_filename)

    text_filename = os.path.join(path, "testo.txt")
    if os.path.exists(text_filename):
        os.remove(text_filename)

    with open(text_filename, "w") as writer:
        writer.write("Testo casuale di prova")

    zip_file = zipfile.ZipFile(zip_filename, "w")
    zip_file.write(text_filename)

    text_filename_2 = os.path.join(path, "testo2.txt")
    if os.path.exists(text_filename_2):
        os.remove(text_filename_2)

    shutil.move(text_filename, text_filename_2)
    zip_file.write(text_filename_2)

    zip_file.close()


def estrai_zip():
    crea_zip()
    path = "d:\\"
    zip_filename = os.path.join(path, "prova.zip")
    extract_path = os.path.join(path, "estratti")

    zip_file = zipfile.ZipFile(zip_filename, "r")
    zip_file.extractall(extract_path)
    zip_file.extract("testo.txt", extract_path)

    zip_file.close()


def info_zip():
    crea_zip()
    path = "d:\\"
    zip_filename = os.path.join(path, "prova.zip")
    zip_file = zipfile.ZipFile(zip_filename, "r")
    print(zip_file.namelist())

    urlsinfo = zip_file.getinfo(zip_filename)
    urlsinfo.filesize
    urlsinfo.compress_size

    zip_file.close()


if __name__ == "__main__":
    scelta = input(
        """
Scegli cosa vuoi fare:
1 - Creare archivio ZIP
2 - Estrarre file da archivio ZIP
3 - Informazioni archivio ZIP\n"""
    )
    match scelta:
        case "1":
            crea_zip()
        case "2":
            estrai_zip()
        case "3":
            info_zip()
