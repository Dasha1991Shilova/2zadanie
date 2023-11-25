import pandas as pd
from sklearn.preprocessing import StandartScaler
from sklearn.impute import SimpleImputer
from sklern.processing import OneHotEncoder
from sklearn.pipeline import Pipeline

file_path='data.csv'
data=pd.read_cs(file_path)

print(data.info())

imputer=SimpleImputer(strategy='mean')
data_filed=pd.DataFrame(imputer.fit_transform(data),columns=data.columns)

encoder=OneHotEncoder(sparse=False, drop='first')
data_encoded=pd.DataFrame(encoder.fit_transform(data_filed[[name]]),columns=['encoded_category'])

scaler=StandartScaler()
data_scaled=pd.DataFrame(scaler.fit_transfor m(data_filled[[age]]),columns=['scaled_numeric']}

preprocessed_data=pd.concat([data_encoded,data_scaled,data_filled.drop([name,age],axis=1)
preprocessed_data.to_csv
('preprocessed_data.csv', index=False)

print('Предобработанные данные сохранен в preprocessed_data.csv')

