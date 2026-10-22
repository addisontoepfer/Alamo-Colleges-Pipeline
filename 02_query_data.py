import pandas as pd
import sqlite3

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# 1. Connect to the database
conn = sqlite3.connect('alamo_enrollment.db')
df = pd.read_sql_query("SELECT * FROM raw_enrollments;", conn)

print("--- 1. THE BLUEPRINT (Data Types & Non-Null Counts) ---")
print(df.info())

print("\n--- 2. THE STATS (Outliers & Averages) ---")
# .describe() only looks at numbers. It will show us if GPA or Credits have weird extremes.
print(df.describe())

print("\n--- 3. MISSING VALUE TOTALS ---")
# This scans ALL columns for NULLs, not just the ones we expect.
print(df.isnull().sum())

print("\n--- 4. DUPLICATE ROWS ---")
# Scans the entire dataset for exact copy-paste rows
print(f"Total exact duplicate rows: {df.duplicated().sum()}")

print("\n--- 5. LOGICAL CHECKS (Status vs Grade) ---")
# Cross-tabulation to build a matrix showing the relationship between two columns.
print(pd.crosstab(df['Enrollment_Status'], df['Final_Grade']))

conn.close()