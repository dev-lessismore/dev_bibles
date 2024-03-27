dev-lessismore
bp&mJhnF3MJY#Q


---Installazione---
	Git
		https://git-scm.com/download/win
		brew install git
	CLI
		https://cli.github.com/
		brew install gh
		brew upgrade gh
	
	
---Configurazione globale e Login---
	git --version
	git config --global user.name 'dev-lessismore'
	git config --global user.email dev.lessismore@gmail.com
	
	gh auth login 
		scegliere github.com
		https
		e fare login sul browser
		
---Il file .gitignore---
	https://github.com/github/gitignore
	
---Comandi---
git init
git add nome_file
git add .			(attenzione a come usarlo!)
git reset nome_file (rimuovo un file)
git commit -m "UPDATE post views to convert markdown post content to HTML"
				"[CHIAVE_ESPLICITA] [descreizione concisa in inglese e specifica]"
				
git log				(lista dei commit, per uscire premere Q)				
git push			(caricare i commit locali su un repository)
git pull			(recupera le modifiche dal repository)
git fetch			(scarica e visualizza le modifiche senza applicarle)
git clone [url]		(clona il repository in locale)
git revert xyzt421	(nuovo commit che annulla le modifiche dal commit xyzt421)
git reset HEAD~1


---Git status---
	Il branch corrente e il commit più recente.
	I file che sono stati modificati ma che non sono ancora stati aggiunti alla staging area.
	I file che sono stati aggiunti alla staging area, ma di cui ancora non si è effettuato il commit.
	I file che sono stati eliminati dalla working directory, ma non sono stati ancora eliminati dalla staging area.


---Nuovo branch del progetto---
	git branch feature-X 		(creazione del branch)
	git checkout feature-X		(attivare il branch)
	git merge feature-X			(da fare dal branch master)

---Pull Request---
	Creare un fork del progetto su GitHub
	Clonare il repo del fork sul proprio computer
	Creare un branch su cui apportare delle modifiche
	Salvare le modifiche via commit nel branch
	Pubblicare le modifiche sul ramo del proprio fork via push
	Aprire una pull request
		
	
	
---Esempio operativo---
	git clone https://github.com/dev-lessismore/py_calculator.git
	git status				(ci dirà che siamo sul main branch, senza modifiche)
	// modifichiamo il file calculator.py
	git add .\calculator.py
	git status				(ci dirà che siamo sul main branch, segnala modifica al file)
	git commit -m "UPDATE welcome message"
	git push
	// creo il file README.md dal sito di GitHub
	git pull
	// modifico il file README.md
	git fetch
	git diff origin/main	(mostra le modifiche fatte al file README.md)
	git pull
	git log					(elenco di tutti i commit fatti)
	
	
	git branch module-implementation
	git checkout module-implementation		(oppure git checkout -b module-implementation)
	git push origin module-implementation
	// modifichiamo il file calculator.py
	git add calculator.py
	git push origin module-implementationd
	// facciamo il merge su main delle modifiche
	git checkout main
	git merge module-implementation
	git push
