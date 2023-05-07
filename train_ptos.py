import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import datetime
import pickle

df = pd.read_csv('./data/GLODAPv2 Merged Master File.csv')

# Modelo para la prediccion de puntos de muestreo
df = df[['latitude', 'longitude', 'pressure','temperature', 'salinity', 'oxygen', 'nitrate', 'silicate', 'phosphate', 'phts25p0','tco2']]

X = df.drop(['longitude', 'latitude'], axis=1) 
y = df[['longitude', 'latitude']]

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

ptos_model = RandomForestRegressor(n_estimators=100, random_state=42)
ptos_model.fit(X_train, y_train)

utils_folder = os.path.join(os.getcwd(), "utils")
now = datetime.datetime.now().strftime("%y%m%d%H%M%S")
filename2 = os.path.join(utils_folder, f"ptos_model_{now}.pkl")

with open(filename2, 'wb') as file2:
    pickle.dump(ptos_model, file2)

print(f"Modelo entrenado guardado como {filename2}")