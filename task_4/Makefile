clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	pip install -e .[dev] --upgrade --no-cache

install:
	pip install -e .['dev']


init_db:
	#FLASK_APP=projeto/app.py flask db init
	#FLASK_APP=projeto/app.py flask create-db
	FLASK_APP=projeto/app.py flask db upgrade
	# FLASK_APP=projeto/app.py flask populate-db

routes:
	FLASK_APP=projeto/app.py flask routes

format:
	isort **/*.py
	black -l 79 **/*.py

run:
	FLASK_APP=projeto/app.py FLASK_ENV=development flask run