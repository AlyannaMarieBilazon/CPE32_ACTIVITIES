#If else statement

score = int(input("Enter the student's score: "))

if score > 90:
    grade = "A"
elif score > 75:
    grade = "B"
elif score > 65:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)