-- Django --
	pip install django
	pip install mssql-django
	pip install django-crispy-forms
	pip install crispy-bootstrap5
		CRISPY_TEMPLATE_PACK = "bootstrap5"
	django-admin startproject nome_progetto
	python3 manage.py runserver
	python3 manage.py startapp [nome_app]
	# settings.py -> includere la nuova app
	import os.path
	os.path.join(BASE_DIR, 'accounts/templates')
	# urls.py -> includere il file
	./app/models.py # definisco la classi modello 
	python3 manage.py makemigrations
	python3 manage.py sqlmigrate [nome_app] [n_migrazione]
	python3 manage.py migrate # è il comando che scrive il db
	python3 manage.py inspectdb > models_test.py [tabella_1] [tabella_2] # crea modelli a partire da tabelle esistenti

	python manage.py changepassword <username>
		
	-- Django Database API Create Retrive Update Delete CRUD --
		python3 manage.py shell
		rom news.models import [Tabella]
		variabile = [Tabella].objects.all()
		g1 = [Tabella](nome="Mario", cognome="Rossi")
		g1.save()
		variabile = [Tabella].objects.get(pk=1)
		variabile = [Tabella].objects.filter(nome="Mario")
		variabile = [Tabella].objects.exclude(pk=1)
		for g in [Tabella].objects.all()
		[variabile].delete()
		[variabile].[related_name].all() # tutti i record collegati tramite fkA
	
	-- Django Test --
		python3 manage.py test --verbosity=2



-- Models --
	from django.db import models
	from django.contrib.auth.models import User
	from django.core.validators import MinValueValidator, MaxValueValidator



	class Profile(models.Model):
		rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
		ebook = models.ForeignKey(Ebook,on_delete=models.CASCADE,related_name="reviews")


-- Djangi Shell --
	python manage.py shell
ß
	from questions.models import Question
	from users.models import CustomUser

	u = CustomUser.objects.first()
	u
	q = Question.objects.create(content="Funziona??", author = u)
	q.slug

	quit()