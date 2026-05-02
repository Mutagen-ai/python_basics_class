#Numpy Essentials
import numpy as np

# 1. Create the grades array
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

print("=" * 50)
print("       STUDENT GRADES ANALYSIS REPORT")
print("=" * 50)
print(f"\nOriginal Grades: {grades}")

# 2. Statistical measures
mean   = np.mean(grades)
median = np.median(grades)
std    = np.std(grades)

print("\n--- Statistical Measures ---")
print(f"  Mean:               {mean:.2f}")
print(f"  Median:             {median:.2f}")
print(f"  Standard Deviation: {std:.2f}")

# 3. Maximum and minimum
max_grade = np.max(grades)
min_grade = np.min(grades)

print("\n--- Max & Min ---")
print(f"  Maximum Grade: {max_grade}")
print(f"  Minimum Grade: {min_grade}")

# 4. Sorted grades
sorted_grades = np.sort(grades)
print("\n--- Sorted Grades (Ascending) ---")
print(f"  {sorted_grades}")

# 5. Index of the highest grade
highest_index = np.argmax(grades)
print("\n--- Highest Grade ---")
print(f"  Index of Highest Grade: {highest_index} (Grade: {grades[highest_index]})")

# 6. Count students who scored above 90
count_above_90 = np.sum(grades > 90)
print("\n--- Students Scoring Above 90 ---")
print(f"  Count: {count_above_90}")

# 7. Percentage of students who scored above 90
pct_above_90 = np.mean(grades > 90) * 100
print(f"  Percentage: {pct_above_90:.1f}%")

# 8. Percentage of students who scored below 75
pct_below_75 = np.mean(grades < 75) * 100
print("\n--- Students Scoring Below 75 ---")
print(f"  Percentage: {pct_below_75:.1f}%")

# 9. Extract grades above 90 → high_performers
high_performers = grades[grades > 90]
print("\n--- High Performers (Grade > 90) ---")
print(f"  Grades: {high_performers}")

# 10. Extract grades above 75 → passing_grades
passing_grades = grades[grades > 75]
print("\n--- Passing Grades (Grade > 75) ---")
print(f"  Grades: {passing_grades}")

print("\n" + "=" * 50)
print("              SUMMARY")
print("=" * 50)
print(f"  Total Students:        {len(grades)}")
print(f"  Passing Students:      {len(passing_grades)}")
print(f"  High Performers:       {len(high_performers)}")
print(f"  Class Average:         {mean:.2f}")
print(f"  Grade Range:           {min_grade} - {max_grade}")
print("=" * 50)