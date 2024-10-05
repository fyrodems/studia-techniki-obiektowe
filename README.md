# studia-techniki-obiektowe

## będzie robione api do autoryzacji

- system autoryzacji oauth
- mają się pojawić obiekty które mają mieć konstruktory
- komentarze

### migracje

- python manage.py makemigrations - tworzenie nowych migracji w oparciu o zmiany w projekcie
- python manage.py migrate - do zastosowywania w projekcie migracji

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
    - odbywa się w INSTALLED_APPS w settings.py
  - migracja (python manage.py migrate)
  - tworzenie uytkownika superuser (python3 manage.py createsuperuser)

### na później

- zrobienie własnych pól które będą dziedziczyć
- wystawić sobie jsona np
- zrobić artykuły, modele (potem zddecydujemy, które mają być przed autoryzacją, a które po)
- widoki
