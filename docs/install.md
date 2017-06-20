### Install

To install `virtualenv`on a Debian, Ubuntu or Mint machine, do:

	sudo apt-get install virtualenv

Then:

	virtualenv venv -p python3
	source venv/bin/activate

	pip install -r requirements.txt

If you want to run this for development, or for local tests, also do:

	pip install -r requirements-dev.txt
