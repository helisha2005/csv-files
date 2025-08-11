# csv-files
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('sales_data.csv')


print(data.head())


summary = data.describe()
print(summary)


total_sales = data.groupby('Product')['Sales'].sum().reset_index()


plt.figure(figsize=(10, 6))
plt.bar(total_sales['Product'], total_sales['Sales'], color='skyblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


data['Date'] = pd.to_datetime(data['Date'])
sales_trend = data.groupby(data['Date'].dt.to_period('M'))['Sales'].sum().reset_index()


plt.figure(figsize=(10, 6))
plt.plot(sales_trend['Date'].dt.to_timestamp(), sales_trend['Sales'], marker='o', color='orange')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
