import pandas as pd
import sqlite3

# 1. Read the raw CSV into Pandas
df = pd.read_csv('mock_student_data.csv')

# 2. Connect to a local SQLite database (this creates the .db file instantly)
conn = sqlite3.connect('alamo_enrollment.db')

# 3. Dump the raw data into a SQL table
df.to_sql('raw_enrollments', conn, if_exists='replace', index=False)

# 4. Close the connection
conn.close()

print("Raw data successfully loaded into alamo_enrollment.db")