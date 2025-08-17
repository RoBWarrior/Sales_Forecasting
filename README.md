# 📈 Sales Forecasting

This project forecasts future sales based on historical transaction data using [Prophet](https://facebook.github.io/prophet/).  
It takes raw CSV sales data, processes it into a clean format, trains a forecasting model, and generates visual plots for both the forecast and its components (trend, seasonality).

---

## 🔍 Overview

- **Input**: A CSV file containing order dates and total revenue.  
- **Processing**: Data is cleaned, formatted (`ds` and `y` columns), and aggregated by date.  
- **Modeling**: A Prophet model is trained on the processed data.  
- **Output**:  
  - Forecast plot with future predictions and confidence intervals.  
  - Component plot showing trend and seasonality breakdowns.  

---

## 📂 Project Structure

Sales_Forecasting/  
│── main.py              # Main entry point to run the whole pipeline  
│── dataprocessing.py    # Cleans and prepares raw sales data  
│── forecastingmodel.py  # Builds, trains, and forecasts with Prophet  
│── utils.py             # Utility functions (plot saving, etc.)  
│── data/  
│   └── raw_sales.csv    # Input data file (not included in repo)  
│── visuals/             # Generated plots will be saved here  

---

## ⚙️ Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Sales_Forecasting.git
   cd Sales_Forecasting
   ```
2. Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
##▶️ Usage

1. Place your sales data in data/raw_sales.csv.
2. The file must contain at least these two columns:
  -Order Date (e.g., 2023-01-15)
  -Total Revenue (numeric)
3. Run the pipeline:
   ```
   python main.py
   ```
4. Check the outputs in the visuals/ folder:
5. forecast_plot.png → Forecast curve with uncertainty intervals.
6. components_plot.png → Trend and seasonality breakdown.
