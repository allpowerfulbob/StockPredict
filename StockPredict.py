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
