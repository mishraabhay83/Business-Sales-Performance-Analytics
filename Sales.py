import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Updated Dataset (Payment Method added)
np.random.seed(42)
n = 100
data = {
    'OrderID': range(1001, 1001 + n),
    'Product': np.random.choice(
        ['Laptop', 'Headphones', 'Smartwatch', 'Monitor', 'Keyboard'], size=n
    ),
    'PaymentMethod': np.random.choice(
        ['UPI', 'Credit Card', 'Net Banking', 'Cash on Delivery'], size=n
    ),
    'UnitPrice': np.random.choice([1200, 150, 300, 500, 80], size=n),
    'Quantity': np.random.randint(1, 5, size=n),
}

df = pd.DataFrame(data)
df['TotalSales'] = df['UnitPrice'] * df['Quantity']

# Plot Charts
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.set_theme(style='whitegrid')

# Chart 1: Revenue by Product
prod_sales = (
    df.groupby('Product')['TotalSales']
    .sum()
    .reset_index()
    .sort_values(by='TotalSales', ascending=False)
)
sns.barplot(
    data=prod_sales, x='Product', y='TotalSales', ax=axes[0], palette='Blues_r'
)
axes[0].set_title('Revenue by Product ($)')

# Chart 2: Revenue by Payment Method
pay_sales = (
    df.groupby('PaymentMethod')['TotalSales']
    .sum()
    .reset_index()
    .sort_values(by='TotalSales', ascending=False)
)
sns.barplot(
    data=pay_sales,
    x='PaymentMethod',
    y='TotalSales',
    ax=axes[1],
    palette='Purples_r',
)
axes[1].set_title('Revenue by Payment Method ($)')

plt.tight_layout()
plt.savefig('task1_sales_dashboard.png')
plt.show()
