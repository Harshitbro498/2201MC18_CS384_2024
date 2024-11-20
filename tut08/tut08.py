# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/content/infy_stock.csv'  # Replace with your actual path in Colab
df = pd.read_csv(file_path)

# Display the first 10 rows
print(df.head(10))

# Check for missing values
print(df.isnull().sum())

# Fill or drop missing values (based on strategy, here we drop them for simplicity)
df = df.dropna()

print(df.head(10))
# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Plot closing price over time
plt.figure(figsize=(10,6))
plt.plot(df['Date'], df['Close'], label='Closing Price')
plt.title('Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()
import pandas as pd
import mplfinance as mpf

# Load the dataset
file_path = '/content/infy_stock.csv'  # Replace with your actual path in Colab
df = pd.read_csv(file_path)

# Prepare the data for mplfinance (Date as index and in correct format)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Plot the candlestick chart
mpf.plot(df, type='candle', volume=True, style='charles', title='Candlestick Chart for INFY Stock',
         mav=(50, 200), show_nontrading=True)
# Calculate daily return percentage
df['Daily Return %'] = ((df['Close'] - df['Open']) / df['Open']) * 100

# Calculate average, median of daily returns
average_return = df['Daily Return %'].mean()
median_return = df['Daily Return %'].median()

# Calculate the standard deviation of closing prices
std_dev_close = df['Close'].std()

print(f"Average Daily Return: {average_return:.2f}%")
print(f"Median Daily Return: {median_return:.2f}%")
print(f"Standard Deviation of Closing Price: {std_dev_close:.2f}")
# Calculate 50-day and 200-day moving averages
df['50 Day MA'] = df['Close'].rolling(window=50).mean()
df['200 Day MA'] = df['Close'].rolling(window=200).mean()

# Plot closing price along with moving averages
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Closing Price')
plt.plot(df['Date'], df['50 Day MA'], label='50 Day MA')
plt.plot(df['Date'], df['200 Day MA'], label='200 Day MA')
plt.title('Stock Price with 50 and 200 Day Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
# Calculate 30-day rolling standard deviation (volatility)
df['30 Day Volatility'] = df['Close'].rolling(window=30).std()

# Plot volatility
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['30 Day Volatility'], label='30 Day Volatility')
plt.title('30-Day Rolling Volatility')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.legend()
plt.show()
# Identify bullish and bearish trends based on moving averages
df['Trend'] = np.where(df['50 Day MA'] > df['200 Day MA'], 'Bullish', 'Bearish')

# Plot closing price with trend
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Closing Price')

# Highlight bullish and bearish periods
bullish = df[df['Trend'] == 'Bullish']
bearish = df[df['Trend'] == 'Bearish']

plt.scatter(bullish['Date'], bullish['Close'], color='green', label='Bullish', alpha=0.5)
plt.scatter(bearish['Date'], bearish['Close'], color='red', label='Bearish', alpha=0.5)

plt.title('Bullish and Bearish Trends Based on Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
