import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.metrics import mean_absolute_error

# Load sample time series data
df = pd.read_csv("data/raw_sales.csv")
df.columns = ['ds', 'y']  # Prophet needs 'ds' (date) and 'y' (value)
df['ds'] = pd.to_datetime(df['ds'])

df.head()

plt.figure(figsize=(10, 5))
plt.plot(df['ds'], df['y'], marker='o')
plt.title("Monthly Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

model = Prophet()
model.fit(df)

# Forecast for the next 12 months
future = model.make_future_dataframe(periods=12, freq='M')
forecast = model.predict(future)

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

fig1 = model.plot(forecast)
plt.title("Sales Forecast (Next 12 Months)")
plt.tight_layout()
plt.show()

fig2 = model.plot_components(forecast)
plt.tight_layout()
plt.show()

# Join actuals and predictions to compute error
actual = df.set_index('ds')
predicted = forecast.set_index('ds')[['yhat']].join(actual).dropna()

mae = mean_absolute_error(predicted['y'], predicted['yhat'])
print(f"Mean Absolute Error: {mae:.2f}")

fig1.savefig("visuals/forecast_plot.png", bbox_inches='tight')
fig2.savefig("visuals/components_plot.png", bbox_inches='tight')
print("Plots saved in the visuals/ folder.")