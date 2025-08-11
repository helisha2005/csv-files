import pandas as pd
import matplotlib.pyplot as plt

# Load the sales data
data = pd.read_csv('sales_data.csv')

# Display the first few rows of the dataset
print(data.head())

# Data summary
summary = data.describe()
print(summary)

# Grouping data by product and calculating total sales
total_sales = data.groupby('Product')['Sales'].sum().reset_index()

# Plotting total sales by product
plt.figure(figsize=(10, 6))
plt.bar(total_sales['Product'], total_sales['Sales'], color='skyblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Analyzing sales trends over time
data['Date'] = pd.to_datetime(data['Date'])
sales_trend = data.groupby(data['Date'].dt.to_period('M'))['Sales'].sum().reset_index()

# Plotting sales trend
plt.figure(figsize=(10, 6))
plt.plot(sales_trend['Date'].dt.to_timestamp(), sales_trend['Sales'], marker='o', color='orange')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
