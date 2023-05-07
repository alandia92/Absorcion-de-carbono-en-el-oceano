import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import datetime
import pickle

df = pd.read_csv('./data/GLODAPv2 Merged Master File.csv')

# Modelo para la predicción de carbono
df = df[['pressure','temperature', 'salinity', 'oxygen', 'nitrate', 'silicate', 'phosphate', 'phts25p0','tco2']]

X = df.drop(['tco2'], axis=1)
y = df['tco2']
scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

co2_model = RandomForestRegressor(n_estimators=100, random_state=42)
co2_model.fit(X_train, y_train)

utils_folder = os.path.join(os.getcwd(), "utils")
now = datetime.datetime.now().strftime("%y%m%d%H%M%S")
filename = os.path.join(utils_folder, f"co2_model_{now}.pkl")

with open(filename, 'wb') as file:
    pickle.dump(co2_model, file)

print(f"Modelo entrenado guardado como {filename}")
