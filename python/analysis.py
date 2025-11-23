#Data Loading
import pandas as pd
df=pd.read_csv("sales.csv")
print("-----------First 5 Rows-----------")
print(df.head())

# Data Cleaning
df["City"]=df["City"].str.strip().str.title()
df["TotalAmount"]=df["Quantity"]*df["Price"]
print("\n --------Cleaned Data-----------")
print(df.head())
# print(df.columns)

# Data Analysis
total_revenue=df["TotalAmount"].sum()
print("\n The Total Revenue is :",total_revenue)

city_revenue=df.groupby("City")["TotalAmount"].sum()
print("\n Reveue by city:")
print(city_revenue)

product_sales=df.groupby("Product")["Quantity"].sum()
print("\n Sales by Product:")
print(product_sales)

top_customers=df.groupby("CustomerName")["TotalAmount"].sum().sort_values(ascending=False).head(3)
print("\n Top 3 Customers:")
print(top_customers)

status_counts=df["Status"].value_counts()
print("\n Order Status Counts:")
print(status_counts)



# Data Visualization
import matplotlib.pyplot as plt

city_revenue = df.groupby("City")["TotalAmount"].sum()

plt.figure(figsize=(8,5))
city_revenue.plot(kind="bar", color="skyblue")
plt.title("City-wise Revenue")
plt.xlabel("City")
plt.ylabel("Total Revenue")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()

product_qty = df.groupby("Product")["Quantity"].sum()

plt.figure(figsize=(7,7))
product_qty.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Product-wise Sales Share")
plt.ylabel("")
plt.show()

df["Month"] = pd.to_datetime(df["OrderDate"]).dt.month

month_rev = df.groupby("Month")["TotalAmount"].sum()

plt.figure(figsize=(8,5))
month_rev.plot(kind="line", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()


plt.hist(df["TotalAmount"], bins=5)
plt.title("Revenue Distribution")
plt.xlabel("Order Amount")
plt.ylabel("Frequency")
plt.show()


import seaborn as sns

pivot = df.pivot_table(values="TotalAmount", index="City", columns="Product", aggfunc="sum")
sns.heatmap(pivot, annot=True, cmap="Blues")
plt.title("City vs Product Revenue Heatmap")
plt.show()
