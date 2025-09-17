# Import required libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import plotly.graph_objects as go

# Load Data file
data = pd.read_csv('c:/users/allpo/desktop/content/stock_data.csv', parse_dates=['Date'])
data.set_index('Date', inplace=True)

# Select the target
# Change this based on the target column
target_column = st.selectbox("Select the target column for predition", options=['AMZN', 'DPZ', 'BTC',
                                                                                'NFLX'])
x = data[['DPZ', 'BTC', 'NFLX']]
y = data[target_column]

# Split the data
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=42)

# Train a simple model
model = RandomForestRegressor(n_estimaotrs=100, random_state=42)
model.fit(x_train, y_train)

# Make predictions on validation data
val_predictions = model.predict(x_val)
mse = mean_squared_error(y_val, val_predictions)
st.write(f"Validation Mean Squared Error: {mse}")

# Sidebar for user input to select forecast horizon
st.sidebar.header("Forecast Settings")
future_days = st.sidebar.slider("Select Future Prediction Days (1-30)", min_value=1, max_value=30,
                                value=7)

# Predict future stock prices for the selected period
last_known_date = data.index[-1]
future_dates = [last_known_date + timedelta(days=i) for i in range(1, future_days + 1)]
future_predictions = model.predict(x.tail(future_days))

# Plotting
st.header(f"{target_column} Stock Price Prediction")
st.write(f"Forecasting the nest {future_days} days")

# Create figure
fig = go.Figure()

# Plot historical data (last 2-3 years)
# Adjust to show more years if needed
years_back = 3
start_date = last_known_date - timedelta(days=365 * years_back)
historical_data = data[target_column].loc[start_date:]
fig.add_trace(go.Scatter(
    x=historical_data.index,
    y=historical_data,
    mode='lines',
    name='Historical Data',
    line=dict(color='green')
))

# Plot future predictions
fig.add_trace(go.Scatter(
    x=future_dates,
    y=future_predictions,
    mode='lines+markers',
    name='Future Prediction',
    line=dict(color='red', dash='dash')
))

# Customize layout
fig.update_layout(
    title=f"{target_column} Stock Price Prediction (Next {future_days} Days)",
    xaxis_title="Date",
    yaxis_title="Price",
    template="plotly_white"
)

# Show plot
st.plotly_chart(fig, use_container_width=True)