#!/bin/bash

cd ..
echo "attivo l'env"
. venv/bin/activate

pip install --upgrade -r requirements/requirements.txt

