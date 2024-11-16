import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import sqlite3


conn = sqlite3.connect("CostOfLiving.db")

# Create a cursor object
cursor = conn.cursor()

cursor.execute("SELECT * FROM ShelterForm")
data = cursor.fetchall()

# Step 1: Load and prepare the data
# file_path = "MOCK_DATA.json"  # Replace with your file path
# data = pd.read_json(file_path)

data = pd.DataFrame(
    data,
    columns=[
        "firstName",
        "lastName",
        "phone",
        "address",
        "email",
        "situation",
        "duration",
        "dueDate",
        "amount",
    ],
)

# Convert dueDate to datetime and aggregate amounts by date
data["dueDate"] = pd.to_datetime(data["dueDate"], format="%m/%d/%Y")
data["amount"] = pd.to_numeric(data["amount"])

aggregated_data = data.groupby("dueDate")["amount"].sum().reset_index()


# Sort by date for time series analysis
aggregated_data = aggregated_data.sort_values("dueDate")

# Step 2: Fit the ARIMA model
arima_model = ARIMA(aggregated_data["amount"], order=(5, 1, 0))
arima_result = arima_model.fit()

# Step 3: Forecast the next 90 days (3 months)
forecast = arima_result.get_forecast(steps=90)
forecast_values = forecast.predicted_mean

# Separate predictions for 7 days, 3 weeks (21 days), and 3 months (90 days)
forecast_7_days = forecast_values[:7]
forecast_3_weeks = forecast_values[:21]
forecast_3_months = forecast_values


def create_l(list):
    chunk_size = len(list) // 3

    # Split the series into 3 parts
    parts = [list[i * chunk_size : (i + 1) * chunk_size] for i in range(3)]

    # Sum each part
    sums = [part.sum() for part in parts]

    # Increase sums partly according to their place
    sums = [round(sum * (1 + i * 0.1)) for i, sum in enumerate(sums)]

    return sums


print(forecast_7_days.round().to_list())
print(create_l(forecast_3_months))
print(create_l(forecast_3_weeks))


##
