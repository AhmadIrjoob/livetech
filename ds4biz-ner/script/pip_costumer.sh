#!/bin/bash                                                                                                                                                          

cd ..
echo attivo venv
. venv/bin/activate
echo cerco di installare $1
pip install $1

echo update requirements
pip freeze > requirements/requirements.txt


