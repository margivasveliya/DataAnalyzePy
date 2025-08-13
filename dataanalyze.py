import pandas as pd
import matplotlib.pyplot as plt


sales_data = pd.read_csv('sales.csv')

print(" First few rows of our sales data:")
print(sales_data.head())


print("\nℹ Basic info about the dataset:")
print(sales_data.info())


print("\n Quick statistics about the sales numbers:")
print(sales_data.describe())


sales_by_product = sales_data.groupby('Product')['Sales'].sum()

print("\n Total sales for each product:")
print(sales_by_product)


sales_by_product.plot(kind='bar', color='orange', title='Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()


if 'Date' in sales_data.columns:
    
    sales_data['Date'] = pd.to_datetime(sales_data['Date'])

    
    monthly_sales = sales_data.groupby(sales_data['Date'].dt.month)['Sales'].sum()

    print("\n Monthly sales totals:")
    print(monthly_sales)

    
    monthly_sales.plot(kind='line', marker='o', color='green', title='Monthly Sales Trend')
    plt.xlabel('Month Number')
    plt.ylabel('Total Sales')
    plt.show()
