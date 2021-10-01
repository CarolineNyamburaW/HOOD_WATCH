serve: 
	python3 manage.py runserver

commit:
	git add .
	git commit -m "made changes"
	git push 

migrations:
	python3 manage.py makemigrations ${app}

migrate:
	python3 manage.py migrate

heroku:
	git add .
	git commit -am "made changes"
	git push heroku main
