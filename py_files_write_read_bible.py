def open_close():
    file_name = "d:\prova.txt"

    # Scrittura file
    file_to_write = open(file_name, "w")
    file_to_write.write("Nuovo file di testo")
    file_to_write.close()

    file_to_write = open(file_name, "a")
    file_to_write.write(" ++++ testo aggiunto in riga")
    file_to_write.write("\nriga aggiuntiva 1")
    file_to_write.write("\nriga aggiuntiva 2")
    file_to_write.close()

    # Lettura File
    var_lettura = open(file_name, "r").read()
    print(var_lettura)

    var_lista_lettura = open(file_name, "r").readlines()
    print(var_lista_lettura)

    file_to_read = open(file_name, "r")
    riga = file_to_read.readline()
    while riga != "":
        print(riga)
        riga = file_to_read.readline()
    file_to_read.close()

def with_open():
    ######## with open ########
    file_name = "d:\prova2.txt"
    with open(file_name, "w") as my_file:
        my_file.write("Hello world \n")
        my_file.write("I hope you're doing well today \n")
        my_file.write("This is a text file \n")
        my_file.write("Have a nice time \n")

    with open(file_name, "a") as my_file:
        my_file.write("riga aggiuntiva 1 \n")
        my_file.write("riga aggiuntiva 2 \n")

    stringa_lunga = ['testo lungo',' in formato',' lista']
    with open(file_name, "a") as my_file:
        my_file.writelines(stringa_lunga)

    with open(file_name) as my_file:
        print(my_file.read())
    
    with open(file_name) as my_file:
        for line in my_file:
            print(line)


if __name__ == "__main__":
    scelta = input("Premi 1 per metodo open+close, premi 2 per with open ---> ")
    if scelta == "1":
        open_close()
    elif scelta == "2":
        with_open()

    
