## Abstract

Orange County Lettings Website

## Local development

### Requirements

- A github account with read access to this repo
- Git CLI
- SQLite3 CLI
- Python 3.9 or higher
- poetry

#### Clone the repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/ylxdre/OCR-P13-CI-CD.git`

#### Activate virtual environment

- `cd /path/to/OCR-P13-CI-CD`
- `poetry env use python3.11`
- `poetry env activate` and run the command displayed
- To deactivate, just run `deactivate`

#### Launch the site

- `cd /path/to/OCR-P13-CI-CD`
- `poetry env activate` and run the command displayed 
- `poetry add $(cat requirements.txt)`
- `python manage.py runserver`
- Then go on `http://localhost:8000` in your favorite browser

#### Linting

- `cd /path/to/OCR-P13-CI-CD`
- `poetry run flake8`

#### Unit tests

- `cd /path/to/OCR-P13-CI-CD`
- `poetry run pytest -v`

#### Database

- `cd /path/to/OCR-P13-CI-CD`
- execute `sqlite3` to open a shell session (requires the sqlite3 package installed)
- then connect to the database `.open oc-lettings-site.sqlite3`
- display the tables by typing  `.tables`
- display columns in the profiles table, `pragma table_info(OCR-P13-CI-CD_profile);`
- make a query on the profiles table, `select user_id, favorite_city from
  OCR-P13-CI-CD_profile where favorite_city like 'B%';`
- type `.quit` to exit

