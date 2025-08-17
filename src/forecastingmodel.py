from prophet import Prophet
import matplotlib.pyplot as plt

def train_model(df):
    model = Prophet()
    model.fit(df)
    return model

def make_forecast(model, periods=12):
    future = model.make_future_dataframe(periods=periods, freq='M')
    forecast = model.predict(future)
    return forecast

def plot_forecast(model, forecast):
    fig = model.plot(forecast)
    plt.title("Sales Forecast")
    plt.savefig("visuals/forecast_plot.png")
    return fig

def plot_components(model, forecast):
    fig = model.plot_components(forecast)
    plt.savefig("visuals/components_plot.png")
    return fig
