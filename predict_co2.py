import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import os

model_file = "utils/co2_model_230507114929.pkl"
with open(model_file, 'rb') as file:
    co2_model = pickle.load(file)

df = pd.read_csv('./data/GLODAPv2 Merged Master File.csv')

df = df[['pressure','temperature', 'salinity', 'oxygen', 'nitrate', 'silicate', 'phosphate', 'phts25p0','tco2']]

X = df.drop(['tco2'], axis=1)
y = df['tco2']
scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

y_pred = co2_model.predict(X_test)

dfco2_pred = pd.DataFrame({'tco2_real': y_test,
                        'tco2_pred': y_pred})


data_folder = os.path.join(os.getcwd(), "data")
output_file = os.path.join(data_folder, f"co2_predictions.csv")

dfco2_pred.to_csv(output_file, index=False)

print(f"Predicciones guardadas como {output_file}")
