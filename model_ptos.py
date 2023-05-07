import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import pickle

df = pd.read_csv('./data/GLODAPv2 Merged Master File.csv')

# Modelo para la prediccion de puntos de muestreo
df = df[['latitude', 'longitude', 'pressure','temperature', 'salinity', 'oxygen', 'nitrate', 'silicate', 'phosphate', 'phts25p0','tco2']]

X = df.drop(['longitude', 'latitude'], axis=1) 
y = df[['longitude', 'latitude']]

scaler = StandardScaler()
X = scaler.fit_transform(X)

ptos_model = RandomForestRegressor(n_estimators=100, random_state=42)
ptos_model.fit(X, y)

production_folder = os.path.join(os.getcwd(), "production")
if not os.path.exists(production_folder):
    os.makedirs(production_folder)
filename2 = os.path.join(production_folder, f"ptos_model.pkl")

with open(filename2, 'wb') as file2:
    pickle.dump(ptos_model, file2)

print(f"Modelo entrenado termiando guardado como {filename2}")