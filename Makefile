install: venv
	pip3 install -Ur requirements.txt
	. venv/bin/activate

venv :
	test -d venv || virtualenv venv

clean:
	rm -rf venv
	find -iname "*.pyc" -delete