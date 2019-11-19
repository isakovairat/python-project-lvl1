install:
		poetry install

build:
		poetry build

publish:
		poetry publish -r testpypi

lint:
		poetry run flake8 brain_games

.PHONY: install build publish lint