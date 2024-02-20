# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u0UlZoz9gK1w9okBpNrQ6LBxqYnhBx5j
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
df = pd.read_csv('VTIdata.csv')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sort DataFrame by date in ascending order
df = df.sort_values(by='Date')

# Initialize variables
investment_value = 0
initial_value = 100
principle_investment = initial_value  # Principle investment is the initial value

# Lists to store buy points
buy_dates = []
buy_prices = []

# Loop through the DataFrame
for i in range(len(df) - 6):
    # Calculate the percentage change over the 7-day period
    percentage_change = ((df.iloc[i]['Close/Last'] - df.iloc[i + 6]['Close/Last']) / df.iloc[i + 6]['Close/Last']) * 100

    # Check if the percentage change is <= -2%
    if percentage_change <= -3:
        # Store buy points
        buy_dates.append(df.iloc[i]['Date'])
        buy_prices.append(df.iloc[i]['Close/Last'])

        # Calculate how much of the investment to buy
        bought_amount = initial_value / df.iloc[i]['Close/Last']
        investment_value += bought_amount

# Multiply the final investment value by the last share price to get the total end value
total_end_value = investment_value * df.iloc[-1]['Close/Last']

# Calculate the percent growth
percent_growth = ((total_end_value - principle_investment) / principle_investment) * 100

# Plot VTI data
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Close/Last'], label='VTI')

# Plot buy points
plt.scatter(buy_dates, buy_prices, color='red', label='Buy Points')

plt.title('VTI with Virtual Buys')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

# Print the final investment value
print("Total end value:", round(total_end_value, 2))
print("Initial investment:", round(principle_investment, 2))
print("Percent growth:", round(percent_growth, 2), "%")