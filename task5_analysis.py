import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load CSV
df = pd.read_csv("sales.csv")

# Step 2: Explore data
print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe())

# Step 3: Group & Aggregate
sales_by_region = df.groupby("Region")["Sales"].sum()
sales_by_product = df.groupby("Product")["Sales"].sum()

# Convert Date column to datetime for time analysis
df["Date"] = pd.to_datetime(df["Date"])
sales_by_month = df.groupby(df["Date"].dt.month)["Sales"].sum()

print("\n--- Sales by Region ---")
print(sales_by_region)

print("\n--- Sales by Product ---")
print(sales_by_product)

print("\n--- Sales by Month ---")
print(sales_by_month)

# Step 4: Plot results
plt.figure(figsize=(8,5))
sales_by_region.plot(kind="bar", color="skyblue")
plt.title("Total Sales by Region")
plt.ylabel("Sales Amount")
plt.xlabel("Region")
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x=sales_by_product.index, y=sales_by_product.values, palette="viridis")
plt.title("Total Sales by Product")
plt.ylabel("Sales Amount")
plt.xlabel("Product")
plt.show()

plt.figure(figsize=(8,5))
sales_by_month.plot(kind="line", marker="o", color="red")
plt.title("Monthly Sales Trend")
plt.ylabel("Sales Amount")
plt.xlabel("Month")
plt.show()
