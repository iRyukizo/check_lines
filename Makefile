RM = rm -rf
PYTHON=python3
SETUP=setup.py
SERVER=pypi
TRASH = check_lines.egg-info dist build

all: upload

upload:
	$(PYTHON) $(SETUP) sdist bdist_wheel
	$(PYTHON) -m twine upload --repository $(SERVER) dist/*

clean:
	$(RM) $(TRASH)
