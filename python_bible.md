---PYTHON---

-- VS Code --
ctrl+shift+P" and type "Python: Clear Workspace Interpreter Settings" AND "Python: Select Interpreter" 

-- Codice --
import random 
from math import sqrt 
import os

if 1>2 :
    do ...
elseif 1>3 .
    do ...
else
    do ...

while i <= 10 :
    if i == 2 :
        print("Jump all'inizio")
    if i == 5 :
        print("Esco")
        break
    print(i)
    i += 1

for i in range (11) :
    print(i) # stampa da 0 a 10, si parte da 0 a il numero 11 è escluso

for i in range (start, stop, step):
    print(i) # start è incluso, stop è escluso

for index, elem in enumerate(a_list):
	print(index, elem)

def funzione_sommatrice(a,b, c=0) : 
    var_risultato = a + b + c
    return risultato # funzioni senza return hanno type=None

class Classe_esempio :
    pass # segnaposto
variabile = Classe_esempio()

Liste (insieme di dati ordinati)
	lista = list()
	lista = []
	lista.append(1)
	lista.append("stringa")
	print(lista[0])

	for x in lista:
		print(x)


Tuple (lista immutabili, più veloce e meno pesanti in memoria)
	tupla = (1,2,"tre")
	print(tupla[2])
	lista = list(tupla)
	
	giorni=("lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica")
	
	print(giorni.index("lunedì") # torna la posizione
	print(giorni.count("lunedì") # conta le occorrenze
	
	if "sabato" in giorni:
		print("Presente")
		
	
Set (lista non ordinate, no duplicati)
	city = { "Milano", "Roma", "Torino" }
	capitali = {"Roma", "Parigi", "Londra"}
	print(city & capitali)
	print(city.intersection(capitali))
	print(city.union(capitali))
	print(capitali - city)
	print(capitali.difference(city))
	

Dizionari (insieme di chiavi:valore, è un array associativo)
	dipendenti = dict()
	dipendenti = { 'Andrea':1182, 'Paolo':1034, 'Mario':1248 }
	dipendenti["Luca"] = 2981
	dipendenti.keys()
	dipendenti.items()
	dipendenti.get(dipendenti.keys()
	if "Andrea" in dipendenti:
		print("Presente!")
	len(dipendenti)


-- Log --
	logging.warning('This is a warning message')
	logging.error('This is an error message')
	logging.critical('This is a critical message')

--- Venv ---	
	python3 -m venv <nome-ambiente-virtuale>
	source <nome-ambiente-virtuale>/bin/activate # deactivate
	.\v_env\Scripts\activate .\v_env\Scripts\deactivate
	Get-ExecutionPolicy
	Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
	
	-- Migrate venv --
	pip freeze > requirements.txt
	copy prj file/folder without venv 
	python3 -m venv v_env
	source v_env/bin/activate
	pip install -r requirements.txt
			 
-- PIP Pulizia ambiente --
	pip freeze > requirements.txt
	pip uninstall -r requirements.txt -y
	pip install -r requirements.txt


-- pyodbc Apple Silicon --
	pip uninstall pyodbc
	export CPPFLAGS="-I/opt/homebrew/Cellar/unixodbc/2.3.9_1/include"
	export LDFLAGS="-L/opt/homebrew/Cellar/unixodbc/2.3.9_1/lib -liodbc -liodbcinst"
	cd path/to/pyodbc-4.0.32.tar.gz
	pip install pyodbc-4.0.32.tar.gz


-- Requirements --
	touch requirements.txt
	python3 -m pip freeze > requirements.txt
	cat requirements.txt


-- cartella_progetto -- 
├── src
│   ├── setup.py
│   └── simple_api
        ├── __init__.py					 
        ├── __main__.py
        └── api.py
└── venv



-- Filesystem -- 