# Secure Banking App
##### An extremely basic banking web app in Flask demonstrating prevention of some the most common cyber attacks

## Installation
recommended [python](https://www.python.org/) v3.10+ to run.

create a vitrual environment for the project
```sh
python3 -m venv env
```

activate the virtual environment
```sh
. env/bin/activate
```

Install the dependencies
```sh
pip install -r dependencies.txt
```

initialize the database using the provided scripts
```sh
python3 bin/create_db.py
```

the .env file should look like this
```
# required
SECRET_KEY=yoursupersecrettokenhere
DB=bank.db
# optional
FLASK_DEBUG=1
FLASK_ENV=development
```

start the dev server
```sh
flask run
```
OR
```sh
python3 app.py
```

run unit-tests
```sh
pytest --verbose
```

