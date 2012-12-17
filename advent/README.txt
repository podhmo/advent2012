advent README
==================

Getting Started
---------------

		cd <directory containing this file>
		$venv/bin/python setup.py develop
		$venv/bin/alembic upgrade head
		$venv/bin/initialize_advent_db development.ini
		$venv/bin/pserve --reload development.ini
