import pandas as pd
import random
import numpy as np

# 1. Setup our variables
num_students = 5000
terms = ['Fall 2025', 'Spring 2026']
courses = ['ENGL-1301', 'MATH-1414', 'HIST-1301', 'BIOL-2401', 'PSYC-2301', 'COSC-1336']
statuses = ['Full-Time', 'Part-Time']
# Weight the grades so it looks realistic (more A's, B's, C's, fewer D's, F's, W's)
grades = ['A', 'B', 'C', 'D', 'F', 'W', np.nan] # Added NaN to simulate missing/dirty data
grade_weights = [0.25, 0.30, 0.20, 0.10, 0.08, 0.05, 0.02]

print("Generating Alamo Colleges mock dataset...")

# 2. Build the data loop
data = []
for i in range(num_students):
    student_id = f"BANNER{random.randint(100000, 999999)}"
    term = random.choice(terms)
    course = random.choice(courses)
    status = random.choices(statuses, weights=[0.6, 0.4])[0] # 60% full-time
    grade = random.choices(grades, weights=grade_weights)[0]
    
    #Dirtying Data
    if course == 'MATH-1414' and random.random() < 0.05:
        course = 'math-1414 ' # lowercase and trailing space
        
    data.append([student_id, term, course, status, grade])

# 3. Create the Pandas DataFrame
df = pd.DataFrame(data, columns=['StudentID', 'Term', 'Course_ID', 'Enrollment_Status', 'Final_Grade'])

# 4. Export to CSV
file_name = 'mock_student_data.csv'
df.to_csv(file_name, index=False)

print(f"Success! Generated {num_students} records and saved to {file_name}.")

