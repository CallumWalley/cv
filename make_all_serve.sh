#!/bin/bash 
source .venv/bin/activate
python make_all.py
python make_index.py
cd docs && python3 -m http.server "$@"