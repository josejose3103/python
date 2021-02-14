
import pandas as pd


import matplotlib.pyplot as plt
from fbprophet import Prophet

data = pd.DataFrame()
file_name = '5794_2021.csv'
data2 = pd.read_csv(file_name, skiprows=1,header=None, names=['ds','Open','High','Low','Close','y','Volume'])

data = data.append(data2)
print(data)

model = Prophet()
model.fit(data)

future_data = model.make_future_dataframe(periods=250, freq = 'd')
future_data = future_data[future_data['ds'].dt.weekday < 5]

forecast_data = model.predict(future_data)

fig = model.plot(forecast_data)
model.plot_components(forecast_data)
