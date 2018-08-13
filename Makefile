venv:
	virtualenv venv --python python3
	. venv/bin/activate && pip install -U requirements.txt

requirements.txt: venv requirements.in
	. venv/bin/activate && pip freeze > requirements.txt
