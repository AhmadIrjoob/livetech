#!/bin/bash

cd ..
virtualenv -p python3 --no-site-packages venv
cd script
sh updateEnv.sh
