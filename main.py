# STEP 1A
# Import SQLITE and pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")
# Add code below and run file to see data from employees table

employee_data = pd.read_sql("SELECT * FROM employees", conn)

# STEP 2
df_first_five = employee_data[['employeeNumber', 'lastName']].head(5)


# STEP 3
# Replace None with your code
df_five_reverse = employee_data[['lastName','employeeNumber']].tail(5)

# STEP 4
# Replace None with your code
df_alias = employee_data.rename(columns={"employeeNumber": "ID"})[["lastName","ID"]].tail(5)


# STEP 5
df_executive = employee_data.copy()
df_executive["role"] = "Not Executive"
df_executive.loc[
    df_executive["jobTitle"].isin(["President", "VP Sales", "VP Marketing"]),
    "role"
] = "Executive"


# STEP 6
# Replace None with your code
df_name_length = employee_data["lastName"].str.len().to_frame(name="name_length")

# STEP 7
# Replace None with your code
df_short_title = employee_data["jobTitle"].str[:2].to_frame(name="short_title")


# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql("""
SELECT ROUND(priceEach * quantityOrdered) AS total_price
FROM orderDetails;
""", conn)["total_price"].sum()


# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql("""
SELECT
    orderDate,
    strftime('%d', orderDate) AS day,
    strftime('%m', orderDate) AS month,
    strftime('%Y', orderDate) AS year
FROM orders;
""", conn)

conn.close()