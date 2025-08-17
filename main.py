# main.py
from src.dataprocessing import load_and_clean_data
from src.forecastingmodel import train_model, make_forecast, plot_forecast, plot_components
from src.utils import save_plot

def main():
    # Load and clean data
    data_path = "data/raw_sales.csv"
    df = load_and_clean_data(data_path)

    # Train model
    model = train_model(df)

    # Forecast future sales
    forecast = make_forecast(model, periods=12)

    # Generate and save forecast plot
    forecast_fig = plot_forecast(model, forecast)
    save_plot(forecast_fig, "forecast_plot.png")

    # Generate and save component plot (trend, seasonality, etc.)
    components_fig = plot_components(model, forecast)
    save_plot(components_fig, "components_plot.png")

if __name__ == "__main__":
    main()
