#!/bin/bash

python3 data_cleaner.py
python3 separate_station.py
python3 separate_saison.py
python3 separate_moment.py
python3 classes_cleaner.py
python3 barycentre.py
python3 dynamique.py
python3 k_means.py
python3 knn.py