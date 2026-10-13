import streamlit as st
import sqlite3
import pandas as pd

st.title("Smart Energy Consumption System")
st.write("Monitor and analyze your monthly electricity usage.")

connection = sqlite3.connect("energy.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS energy_consumption (
    month TEXT PRIMARY KEY,
    units INTEGER,
    bill REAL
)
""")

connection.commit()

data = pd.read_sql_query(
    "SELECT month, units, bill FROM energy_consumption",
    connection
)

connection.close()

st.header("📝 Add Monthly Electricity Data")

with st.form("energy_form"):
    month = st.selectbox(
        "Select Month",
        [
            "January", "February", "March",
            "April", "May", "June",
            "July", "August", "September",
            "October", "November", "December"
        ]
    )

    units = st.number_input(
        "Electricity Units (kWh)",
        min_value=0,
        step=1
    )

    submitted = st.form_submit_button("Save Data")

if submitted:
    connection = sqlite3.connect("energy.db")
    cursor = connection.cursor()

    cursor.execute(
    "INSERT OR REPLACE INTO energy_consumption (month, units, bill) VALUES (?, ?, ?)",
    (month, units, units * 5)
)

connection.commit()
connection.close()

st.success(f"{month} data saved successfully!")

if cursor.rowcount == 0:
        cursor.execute(
            "INSERT INTO energy_consumption (month, units, bill) VALUES (?, ?, ?)",
            (month, units, units * 5)
        )

    connection.commit()
    connection.close()

    st.success(f"{month} data saved successfully!")
    

if not data.empty:
    st.subheader("Energy Dashboard")

    total_units = data["units"].sum()
    average_units = data["units"].mean()
    total_bill = data["bill"].sum()

    col1, col2 = st.columns(2)
    col1.metric("Total Units", f"{total_units} kWh")
    col2.metric("Average Units", f"{average_units:.1f} kWh")

    col3, col4 = st.columns(2)
    col3.metric("Estimated Bill", f"₹{total_bill:.2f}")

    highest_month = data.loc[data["units"].idxmax(), "month"]
    col4.metric("Highest Usage Month", highest_month)

    st.subheader("Energy Saving Suggestions")

    average = data["units"].mean()
    st.subheader("📊 Energy Dashboard")

    total_units = data["units"].sum()
    average_units = data["units"].mean()
    total_bill = data["bill"].sum()

    col1, col2 = st.columns(2)

    col1.metric("Total Units", f"{total_units} kWh")
    col2.metric("Average Units", f"{average_units:.1f} kWh")

    col3, col4 = st.columns(2)

    col3.metric("Estimated Bill", f"₹{total_bill:.2f}")

    highest_month = data.loc[data["units"].idxmax(), "month"]
    col4.metric("Highest Usage Month", highest_month)
    st.subheader("Energy Saving Suggestions")

    average = data["units"].mean()

    if average > 150:
        st.warning("High energy usage! Switch off unused appliances.")
        st.write("Use LED bulbs and energy-efficient appliances.")
    else:
        st.success("Your energy usage is normal.")
        st.write("Continue saving electricity.")
    st.subheader("Monthly Energy Consumption")
    st.dataframe(data)

    st.metric("Total Units", int(data["units"].sum()))
    st.metric("Average Monthly Units", round(data["units"].mean(), 2))

    st.bar_chart(data.set_index("month")["units"])
else:
    st.warning("No energy data found in the database.")