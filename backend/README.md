## Boba Meets Dumpling

This is the backend for the boba meets dumpling site.
The technologies used to build this is:
- django
- sqllite

Used the following [tutorial](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react) as a starter to set up the menu backend

## Spinning Up the Backend
- Make sure you are running the following commands inside root of the `/backend` directory:
1. Make sure you have pipenv installed `pip install pipenv` (Note: you may need to use `pip3`)
2. Activate a new viritual environment `pipenv shell`
3. Make sure you have Django installed `pipenv install django`
4. Navigate into the second `backend` directory
5. Startup server `python3 manage.py runserver` (Note: you may need to use `python` instead)
6. Navigate to `http://localhost:8000`
7. Use `CTRL+C` or `CONTROL+C` to stop the server

To access the admin site:
1. Run `python3 manage.py runserver`
2. Go `http://127.0.0.1:8000/admin/` and enter username: `danang` password: `menu123`