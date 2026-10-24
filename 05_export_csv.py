import sqlite3
import pandas as pd

# 1. Connect to your SQLite database
conn = sqlite3.connect('alamo_enrollment.db')

# 2. Read the clean table into a Pandas DataFrame
df = pd.read_sql_query("SELECT * FROM clean_enrollments", conn)

# 3. Export the DataFrame to a CSV file for Power BI
df.to_csv('clean_alamo_enrollment.csv', index=False)

print("Success: Data exported to clean_alamo_enrollment.csv")

# 4. Close the database connection
conn.close()