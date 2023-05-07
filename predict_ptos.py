import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import os

model_file = 'utils/ptos_model_230507114944.pkl'
with open(model_file, 'rb') as file:
    ptos_model = pickle.load(file)

df = pd.read_csv('./data/GLODAPv2 Merged Master File.csv')


df = df[['latitude', 'longitude', 'pressure','temperature', 'salinity', 'oxygen', 'nitrate', 'silicate', 'phosphate', 'phts25p0','tco2']]

X = df.drop(['longitude', 'latitude'], axis=1) 
y = df[['longitude', 'latitude']]

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

y_pred = ptos_model.predict(X_test)

df_pred = pd.DataFrame({'longitude_real': y_test['longitude'],
                        'latitude_real': y_test['latitude'],
                        'longitude_pred': y_pred[:, 0],
                        'latitude_pred': y_pred[:, 1]})
dfptos_pred = pd.concat([y_test.reset_index(drop=True), pd.DataFrame(y_pred, columns=['longitude_pred', 'latitude_pred'])], axis=1)


data_folder = os.path.join(os.getcwd(), "data")
output_file = os.path.join(data_folder, f"ptos_predictions.csv")

dfptos_pred.to_csv(output_file, index=False)

print(f"Predicciones guardadas como {output_file}")
