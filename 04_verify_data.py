import pandas as pd
import sqlite3

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# 1. Connect to the database
conn = sqlite3.connect('alamo_enrollment.db')

# 2. Grab the NEW clean table
df = pd.read_sql_query("SELECT * FROM clean_enrollments;", conn)

print("--- 1. SCHEMA VERIFICATION ---")
# Proves all columns were successfully converted to snake_case
print(df.info())

print("\n--- 2. MISSING DATA VERIFICATION ---")
# Proves final_grade nulls were filled
print(df.isnull().sum())

print("\n--- 3. CLEAN TEXT VERIFICATION (Course IDs) ---")
# Proves trailing spaces are gone
print(df['course_id'].value_counts().head(5)) 

print("\n--- 4. CATEGORICAL & LOGICAL VERIFICATION ---")
# Proves everything is UPPERCASE and logically sound
print(pd.crosstab(df['enrollment_status'], df['final_grade']))

conn.close()