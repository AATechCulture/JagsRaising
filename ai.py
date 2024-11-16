import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import sqlite3
from datetime import datetime, timedelta


def dash():

    conn = sqlite3.connect("CostOfLiving.db")

    # Create a cursor object
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ShelterForm")
    data = cursor.fetchall()

    cursor.execute("SELECT * FROM StudentTuitionForm")
    student_tution_form = cursor.fetchall()

    cursor.execute("SELECT * FROM Medical")
    medical_form = cursor.fetchall()

    cursor.execute("SELECT * FROM FoodForm")
    food_form = cursor.fetchall()

    # Close the connection
    conn.close()

    # Convert the data to a DataFrame
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

    student_tution_form = pd.DataFrame(
        student_tution_form,
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
            "grade",
            "schoolName",
        ],
    )

    medical_form = pd.DataFrame(
        medical_form,
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
            "hospitalName",
            "disease",
        ],
    )

    food_form = pd.DataFrame(
        food_form,
        columns=[
            "firstName",
            "lastName",
            "phone",
            "address",
            "email",
            "situation",
            "duration",
            "dueDate",
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

    # Start date (today's date)
    start_date = datetime.today()

    # Function to create date keys for next 7 days
    def create_next_7_days(data_x, start_date):
        return {
            (start_date + timedelta(days=i)).strftime("%Y-%m-%d"): value
            for i, value in enumerate(data_x)
        }

    # Function to create date range keys for weekly data
    def create_weekly_keys(data_x, start_date):
        return {
            f"{(start_date + timedelta(weeks=i)).strftime('%Y-%m-%d')} - "
            f"{(start_date + timedelta(weeks=i+1) - timedelta(days=1)).strftime('%Y-%m-%d')}": value
            for i, value in enumerate(data_x)
        }

    # Function to create date range keys for monthly data
    def create_monthly_keys(data_x, start_date):
        return {
            f"{(start_date + timedelta(days=30*i)).strftime('%Y-%m-%d')} - "
            f"{(start_date + timedelta(days=30*(i+1)) - timedelta(days=1)).strftime('%Y-%m-%d')}": value
            for i, value in enumerate(data_x)
        }

    # Generating the key-value mappings
    daily_mapping = create_next_7_days(forecast_7_days.round().to_list(), start_date)
    weekly_mapping = create_weekly_keys(create_l(forecast_3_weeks), start_date)
    monthly_mapping = create_monthly_keys(create_l(forecast_3_months), start_date)

    daily_mapping = [
        {"country": key, "value": value} for key, value in daily_mapping.items()
    ]
    weekly_mapping = [
        {"country": key, "value": value} for key, value in weekly_mapping.items()
    ]
    monthly_mapping = [
        {"country": key, "value": value} for key, value in monthly_mapping.items()
    ]

    medical_aggregated_data = (
        medical_form[["hospitalName", "email"]]
        .groupby("hospitalName")
        .count()
        .reset_index()
    )
    medical_aggregated_data2 = (
        medical_form[["disease", "email"]].groupby("disease").count().reset_index()
    )

    student_tution_form_aggregated_data = (
        student_tution_form[["schoolName", "email"]]
        .groupby("schoolName")
        .count()
        .reset_index()
    )
    student_tution_form_aggregated_data2 = (
        student_tution_form[["grade", "email"]].groupby("grade").count().reset_index()
    )

    student_tution_form_aggregated_data = [
        {"country": row["schoolName"], "value": row["email"]}
        for _, row in student_tution_form_aggregated_data.iterrows()
    ]
    student_tution_form_aggregated_data2 = [
        {"country": row["grade"], "value": row["email"]}
        for _, row in student_tution_form_aggregated_data2.iterrows()
    ]
    medical_aggregated_data = [
        {"country": row["hospitalName"], "value": row["email"]}
        for _, row in medical_aggregated_data.iterrows()
    ]
    medical_aggregated_data2 = [
        {"country": row["disease"], "value": row["email"]}
        for _, row in medical_aggregated_data2.iterrows()
    ]

    return (
        student_tution_form_aggregated_data,
        student_tution_form_aggregated_data2,
        medical_aggregated_data,
        medical_aggregated_data2,
        daily_mapping,
        weekly_mapping,
        monthly_mapping,
    )


if __name__ == "__main__":
    dash()
