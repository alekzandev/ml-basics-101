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

pull:
	git fetch origin &&\
	git pull

getdata:
	python3 x1_get_Data.py

preprocess:
	python3 x2_preprocessing_data.py

train:
	python3 x3_training.py

pipemodel: getdata preprocess