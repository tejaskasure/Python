students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 42},
    {"name": "Charlie", "score": 95},
    {"name": "David", "score": 68},
    {"name": "Eva", "score": 73}
]

passing_students = []
failing_students = []

for student in students:
    name = student["name"]
    score = student["score"]

    # Determine the letter grade
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    # Display student's result
    print(f"{name}: Score = {score}, Grade = {grade}")

    # Separate students into passing and failing lists
    if score >= 50:
        passing_students.append(name)
    else:
        failing_students.append(name)

print("\nPassing Students:")
for name in passing_students:
    print(name)

print("\nStudents Needing Extra Help:")
for name in failing_students:
    print(name)


#output:-
#Alice: Score = 85, Grade = B
#Bob: Score = 42, Grade = F
#Charlie: Score = 95, Grade = A
#David: Score = 68, Grade = D
#Eva: Score = 73, Grade = C

#Passing Students:
#Alice
#Charlie
#David
#Eva

#Students Needing Extra Help:
#Bob