import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import pickle

df = pd.read_csv('./data/GLODAPv2 Merged Master File.csv')

# Modelo para la predicción de carbono
df = df[['pressure','temperature', 'salinity', 'oxygen', 'nitrate', 'silicate', 'phosphate', 'phts25p0','tco2']]

X = df.drop(['tco2'], axis=1)
y = df['tco2']
scaler = StandardScaler()
X = scaler.fit_transform(X)

co2_model = RandomForestRegressor(n_estimators=100, random_state=42)
co2_model.fit(X, y)

production_folder = os.path.join(os.getcwd(), "production")
if not os.path.exists(production_folder):
    os.makedirs(production_folder)
filename = os.path.join(production_folder, f"co2_model.pkl")

with open(filename, 'wb') as file:
    pickle.dump(co2_model, file)

print(f"Modelo entrenado terminado guardado como {filename}")
