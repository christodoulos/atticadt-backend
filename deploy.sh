#!/bin/bash
rsync -avz --delete requirements.txt src wsgi.py ubuntu@ntuacloud:atticadt-backend
ssh ubuntu@ntuacloud 'source ~/atticadt-backend/venv/bin/activate && pip install -r ~/atticadt-backend/requirements.txt'
ssh ubuntu@ntuacloud 'sudo supervisorctl reload'