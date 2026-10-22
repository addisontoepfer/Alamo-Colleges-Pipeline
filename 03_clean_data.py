import pandas as pd
import sqlite3

conn = sqlite3.connect('alamo_enrollment.db')

# 1. Extract the raw data into Pandas
df = pd.read_sql_query("SELECT * FROM raw_enrollments;", conn)

# 2. TRANSFORM: Clean the data
#Standardize Columns: Force all column names to lowercase snake_case
df.columns = df.columns.str.lower()

# Fix typos: Strip accidental hidden spaces from the course_id column
df['course_id'] = df['course_id'].str.strip()

# Standardize Categorical Data: Force text columns to UPPERCASE
df['term'] = df['term'].str.upper()
df['enrollment_status'] = df['enrollment_status'].str.upper()
df['final_grade'] = df['final_grade'].str.upper() # Doing this before fillna ensures uniformity

# Handle NULLs: Fill missing final_grade values with an 'I' (Incomplete)
df['final_grade'] = df['final_grade'].fillna('I')

# 3. LOAD: Push the clean data back into the database as a NEW table
df.to_sql('clean_enrollments', conn, if_exists='replace', index=False)

print("Data cleaned and saved to 'clean_enrollments' table in the database.")

conn.close()