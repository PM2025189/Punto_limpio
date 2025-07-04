import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Chargement des fichiers CSV (adapter les chemins locaux)
puntos_limpios = pd.read_csv("puntos_limpios.csv")
padron = pd.read_csv("padron_municipal.csv")
avisos = pd.read_csv("avisos_ciudadanos.csv")
aire = pd.read_csv("calidad_aire.csv")
problemas_sociales = pd.read_csv("problematicas_sociales.csv")

# Si certains fichiers sont géographiques (ex. parques)
parques = gpd.read_file("parques_jardines.geojson")

# Affichage de base pour contrôle
print(puntos_limpios.head())
print(padron.head())
print(parques.head())