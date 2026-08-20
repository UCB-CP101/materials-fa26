# sample_program.py
# A simple Python program for demonstration

# Import a library
import math

# Define variables
student_name = "John Smith"
course_name = "Introduction to Programming"
assignment_scores = [85, 92, 78, 96, 88]

# Print basic information
print("Student Information")
print("-" * 20)
print(f"Name: {student_name}")
print(f"Course: {course_name}")
print()

# Calculate and display statistics
print("Assignment Scores:", assignment_scores)
average_score = sum(assignment_scores) / len(assignment_scores)
print(f"Average Score: {average_score:.2f}")
print(f"Highest Score: {max(assignment_scores)}")
print(f"Lowest Score: {min(assignment_scores)}")
print()

# Simple calculation
radius = 5
area = math.pi * radius ** 2
print(f"Area of circle with radius {radius}: {area:.2f}")

# Conditional statement
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B" 
elif average_score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Letter Grade: {grade}")

# Simple loop
print("\nCounting to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

print("Program finished!")

# password = "gob ears"