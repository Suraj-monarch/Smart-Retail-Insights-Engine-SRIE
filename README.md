# Smart Retail Insights Engine (SRIE)

An end-to-end Retail Sales Analytics project built using **Python, SQL, Power BI**, and **Pandas**.  
This project delivers actionable insights on customer behavior, product performance, revenue trends, and city-level sales.


## 🚀 Project Overview

This project analyzes **200 retail transactions** across 8 months (Jan–Aug 2024).  
The goal was to build a full analytics pipeline:

- Data cleaning (Python + Pandas)
- SQL database setup & analysis (MySQL)
- Power BI dashboard for interactive insights
- Business recommendations based on real KPIs


## 📊 Power BI Dashboard Highlights

1. **City-wise Revenue**
2. **Product-wise Sales**
3. **Monthly Revenue Trend**
4. **Top Customers by Total Amount**
5. **Order Status Distribution**
6. **Dynamic Filters (Slicers)**

Dashboard built with:
- Custom measures (TotalAmount, MonthName, AvgValue)
- Clean UI, minimalistic theme
- Modern donut/pie/line/bar visuals


## 🧠 Key Business Insights

- **Delhi** is the highest revenue-generating city.
- **Laptop** contributes the maximum revenue (70–75%).
- **Mouse** is the highest-selling product by volume.
- Top repeat customers: *Pooja Nair, Karan Singh, Rajiv Rao*.
- Revenue grows consistently from Jan → Aug.
- **Low cancellation rate**, but Delhi shows small spikes.
- **Monitor** performs well in mid-tier segment.


## 🐍 Python Work (analysis.py)

- Data cleaning (strip, title case, formatting)
- Feature engineering (`TotalAmount`, `Month`, `MonthName`)
- Revenue summarization
- Top customer extraction
- Product-level metrics


## 🗄 SQL Work (MySQL)

- RetailDB setup + table creation
- Data import via wizard
- Aggregations:
  - City revenue
  - Top customers
  - Product demand
  - Status breakdown
  - Monthly trends using `EXTRACT(MONTH FROM OrderDate)`

SQL scripts in `/sql/` folder.


## ✨ Final Result

A complete **Data Analyst portfolio project** with:

- Clean structured data
- Clear BI storytelling
- Python + SQL + Power BI integration
- Realistic business recommendations

This project is recruiter-ready and can be showcased in:
- Resume
- LinkedIn
- Portfolio
- Interviews

---

## 👨‍💻 Author
Project by **Suraj Rathod**  