from django.shortcuts import render
import pandas as pd
import pathlib
from sqlalchemy import create_engine
import os


ROOT = ROOT = os.path.dirname(os.path.dirname(__file__))
def createTable():
    src = r".csv"
    file = list(pathlib.Path(ROOT).glob(src))
    if file !=0:
        df = pd.read_csv(file, delimiter=',')
        engine = create_engine('postgresql://utilisateur:root@localhost:5432/postgres')
