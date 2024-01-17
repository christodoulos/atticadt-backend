#!/bin/bash
rsync -avz --delete requirements.txt src wsgi.py backend@atticadt:flask
ssh backend@atticadt 'source ~/flask/venv/bin/activate && pip install -r ~/flask/requirements.txt'
ssh backend@atticadt 'sudo supervisorctl reload'