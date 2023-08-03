# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:10:19 2023

@author: tellezbeltran.5
"""

import pandas as pd
import numpy as np
#import openpyxl as xl
from re import search
import matplotlib.pyplot as plt
import datetime

text = pd.read_csv('Documents\Movies.csv',encoding='utf-8-sig')
#asignamos indice
text.set_index('C#', drop=True, append=False, inplace=True, verify_integrity=False)
#reemplaza los valores nulo por 0 en todo el DF
text = text.fillna(0)
#ordena los valores ascendentemente
text.sort_values(by='id',ascending=True, inplace=True)
#Convertimos float a entero
text.popularity=(text.popularity*1000)
#eliminamos duplicados
text.drop_duplicates(subset=['id'],inplace=True)
#volvemos a organizar
text.sort_values(by='C#',ascending=True, inplace=True)
#exploramos info de la data
text.info()
#distribucion de variables numericas
desc=text.describe()
#convertimos la serie "release_date" a type date_time
text['release_date'] = pd.to_datetime(text['release_date'], errors='coerce')
#extraer año
text['Año'] = text['release_date'].dt.year
#estudio variable target1
text.original_language.value_counts()
#target1 vs Lenguaje
target1 = text.groupby(by = ['Año','original_language']).adult.count()
#generamos una grafica usando el metodo matplotlib
(target1.tail(11).unstack(level=0).plot.bar())
plt.show()
#mapeamos una serie para convertirla en int
#text['adult'] = text['adult'].map({'False': 0,'True': 1}).astype(int)
    