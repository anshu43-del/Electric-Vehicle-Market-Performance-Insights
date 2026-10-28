import pandas as pd, plotly.express as px, streamlit as st
st.set_page_config(page_title="EV Industry Dashboard", layout="wide")
df = pd.read_csv("data/ev_dataset.csv")

st.title("⚡ EV Industry Analytics Dashboard")
st.sidebar.header("Filters")
yrs = st.sidebar.slider("Year", int(df.Year.min()), int(df.Year.max()), (int(df.Year.min()), int(df.Year.max())))
cats = st.sidebar.multiselect("Category", sorted(df.Category.unique()), sorted(df.Category.unique()))
mk = st.sidebar.multiselect("Manufacturer", sorted(df.Manufacturer.unique()), sorted(df.Manufacturer.unique()))
d = df[df.Year.between(*yrs) & df.Category.isin(cats) & df.Manufacturer.isin(mk)]
if d.empty: st.warning("No data for these filters."); st.stop()

c = st.columns(4)
c[0].metric("Total Sales", f"{d.Annual_Sales.sum():,}")
c[1].metric("Avg Range (km)", f"{d.Range_km.mean():.0f}")
c[2].metric("Avg Battery (kWh)", f"{d.Battery_Capacity_kWh.mean():.1f}")
c[3].metric("Avg Rating", f"{d.Customer_Rating.mean():.2f}")

t1, t2, t3 = st.tabs(["Strategy (Emily)", "Competitive Intel (David)", "Research (Dr. Williams)"])
with t1:
    a, b = st.columns(2)
    a.plotly_chart(px.pie(d.groupby("Category", as_index=False).Annual_Sales.sum(), names="Category",
        values="Annual_Sales", title="Sales by Category", hole=.4), use_container_width=True)
    b.plotly_chart(px.bar(d.groupby("Manufacturer", as_index=False).Annual_Sales.sum().sort_values("Annual_Sales"),
        x="Annual_Sales", y="Manufacturer", orientation="h", title="Leading Manufacturers"), use_container_width=True)
    a.plotly_chart(px.bar(d.groupby("Category", as_index=False).Customer_Rating.mean(), x="Category",
        y="Customer_Rating", title="Satisfaction by Category", range_y=[3,5]), use_container_width=True)
    g = d.groupby(["Year","Category"], as_index=False).Annual_Sales.sum()
    b.plotly_chart(px.line(g, x="Year", y="Annual_Sales", color="Category", markers=True,
        title="Sales Growth by Category"), use_container_width=True)
with t2:
    a, b = st.columns(2)
    a.plotly_chart(px.pie(d.groupby("Manufacturer", as_index=False).Annual_Sales.sum(), names="Manufacturer",
        values="Annual_Sales", title="Market Share"), use_container_width=True)
    b.plotly_chart(px.pie(d.groupby("Battery_Type", as_index=False).Annual_Sales.sum(), names="Battery_Type",
        values="Annual_Sales", title="Battery Technology Share", hole=.4), use_container_width=True)
    a.plotly_chart(px.bar(d.groupby("Manufacturing_Country", as_index=False).Annual_Sales.sum(),
        x="Manufacturing_Country", y="Annual_Sales", title="Sales by Manufacturing Country"), use_container_width=True)
    b.plotly_chart(px.scatter(d.groupby("Manufacturer", as_index=False).agg(Sales=("Annual_Sales","sum"),
        Rating=("Customer_Rating","mean"), Price=("Price_USD","mean")), x="Price", y="Rating", size="Sales",
        color="Manufacturer", title="Price vs Rating (bubble = sales)"), use_container_width=True)
with t3:
    a, b = st.columns(2)
    a.plotly_chart(px.box(d, x="Battery_Type", y="Range_km", title="Range by Battery Type"), use_container_width=True)
    b.plotly_chart(px.line(d.groupby(["Year","Battery_Type"], as_index=False).Range_km.mean(), x="Year",
        y="Range_km", color="Battery_Type", markers=True, title="Range Trend"), use_container_width=True)
    a.plotly_chart(px.scatter(d, x="Battery_Capacity_kWh", y="Range_km", color="Category",
        title="Capacity vs Range"), use_container_width=True)
    b.plotly_chart(px.density_heatmap(d, x="Manufacturing_Country", y="Battery_Type", z="Annual_Sales",
        histfunc="sum", title="Battery Tech by Production Country"), use_container_width=True)
st.caption("Data is synthetic for demonstration. Replace data/ev_dataset.csv with real data using the same columns.")
