#!/bin/bash 

python3 make_all.py
python3 make_index.py
cd docs && python3 -m http.server