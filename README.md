# studia-techniki-obiektowe

## będzie robione api do autoryzacji

- system autoryzacji oauth
- mają się pojawić obiekty które mają mieć konstruktory
- komentarze

### na dzisiaj

- wirtualna zmienna środowiskowa (venv)
  - python3 -m venv .venv
  - ./.venv/Scripts/activate (windows) || source .venv/bin/activate (mac)
  - pip install Django
- postawienie django

  - django-admin startproject api_project .
  - django-admin startapp api_app
  - python3 manage.py runserver
  - rejestracja aplikacji w projekcie

    <!-- INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api-app'
    ] -->

- migracja  (python manage.py migrate)
- tworzenie uytkownika superuser (python3 manage.py createsuperuser)


- zrobieie własnych pól które będą dziedziczyć
- wystawić sobie jsona
- artykuły, modele (potem zddecydujemy, które mają być przed autoryzacją, a które po)
- 

