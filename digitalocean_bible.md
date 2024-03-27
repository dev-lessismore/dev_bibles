˜
edo!2022Ardo

104.248.173.225

Andrea dag!2023

http://104.248.173.225/admin/
http://104.248.173.225/media/20e2b6_922cfadc18ad4847a560ff24d6f04127mv2.jpg_hkdYPV6.webp
http://104.248.173.225/media/app-release.apk


-- SSH --
    ssh root@104.248.173.225
    sudo apt-get update
    sudo apt-get upgrade    
    pwd #cartella corrente
	sudo shutdown -r now


    -- nuovo account utente --
        adduser django                  edo!2022Ardo
        gpasswd -a django sudo
		sudo useradd -m -d /home/django django
        sudo su - django
        whoami
    
    -- crezione ambiente (nella /home/django con utente django) --
	sudo apt install -y python3-venv
    python3 -m venv django_venv
    source django_venv/bin/activate
    pip install django djangorestframework pillow


-- APPLICATIVI --
	gunicorn #Python WSGI HTTP server
	supervisor #Tool per check&maintain del servizio
	NGINX #gestione dei file statici e media

-- FILE settings.py --
    DEBUG = False
    ALLOWED_HOSTS = ['*']


STATICFILES_DIRS = [BASE_DIR / 'static-storage'] 
STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR / 'media-serve' 
MEDIA_URL = '/media/'
	
	
-- Gunicorn WSGI --
	pip install gunicorn
	gunicorn realestate.wsgi:application --bind 0.0.0.0:8001 #per testate gunicord (nella cartella del progetto)
	nano gunicorn_start.bash #nella home dell'utente (file di configurazione gunicorn)
	sudo chmod u+x gunicorn_start.bash #rende eseguibile il file
	./gunicorn_start.bash #per eseguire e testate il file
	
	
-- Supervisor --
	sudo apt-get install supervisor
	sudo nano /etc/supervisor/conf.d/realestate.conf #file di configurazione supervisor
	mkdir -p /home/django/logs/
	touch /home/django/logs/gunicorn_supervisor.log
	sudo systemctl restart supervisor
	sudo systemctl enable supervisor
	
	sudo supervisorctl status realestate #check del processo
	


-- NGINX --
	sudo apt-get install nginx
	mkdir static-serve #Nella home dell'utente
	
	--> editare settings.py 
		aggiungendo STATIC_ROOT 
	
	sudo rm /etc/nginx/sites-available/default
	sudo rm /etc/nginx/sites-enabled/default
	
	sudo nano /etc/nginx/sites-available/realestate.conf #file di configurazione 
	sudo ln -s /etc/nginx/sites-available/realestate.conf /etc/nginx/sites-enabled/realestate.conf #link simbolico
	
	python3 manage.py collectstatic #dalla cartella del progetto per copiare i file 
	
	sudo service nginx start
	sudo service nginx restart

	sudo service nginx stop
	
	chmod og+x /home/django/