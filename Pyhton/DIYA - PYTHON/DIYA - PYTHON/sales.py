import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create sample sales data
data = {
    'Date': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
    'Product': np.random.choice(['Laptop', 'Phone', 'Tablet', 'Watch'], size=365),
    'Sales': np.random.randint(1, 100, size=365),
    'Revenue': np.random.randint(100, 1000, size=365)
}

# Create DataFrame
df = pd.DataFrame(data)

# Basic data analysis
def analyze_sales():
    # Calculate total sales by product
    product_sales = df.groupby('Product')['Sales'].sum()
    
    # Calculate monthly revenue
    monthly_revenue = df.groupby(df['Date'].dt.month)['Revenue'].sum()
    
    # Calculate average daily sales
    avg_daily_sales = df.groupby('Product')['Sales'].mean()
    
    # Visualize the data
    plt.figure(figsize=(15, 5))
    
    # Plot 1: Total sales by product
    plt.subplot(1, 3, 1)
    product_sales.plot(kind='bar')
    plt.title('Total Sales by Product')
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    
    # Plot 2: Monthly revenue
    plt.subplot(1, 3, 2)
    monthly_revenue.plot(kind='line', marker='o')
    plt.title('Monthly Revenue')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    
    # Plot 3: Average daily sales by product
    plt.subplot(1, 3, 3)
    avg_daily_sales.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Average Daily Sales Distribution')
    
    plt.tight_layout()
    plt.show()
    
    # Print summary statistics
    print("\nSummary Statistics:")
    print("\nTotal Sales by Product:")
    print(product_sales)
    print("\nMonthly Revenue:")
    print(monthly_revenue)
    print("\nAverage Daily Sales by Product:")
    print(avg_daily_sales)

if __name__ == "__main__":
    analyze_sales()