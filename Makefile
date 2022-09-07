install:
	pip install --upgrade pip &&\
	pip install --upgrade setuptools &&\
	pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C *.py

test:
	python -m pytest -vv --cov=. *.py

push:
	git add . &&\
	git commit -m "Update" &&\
	git push
