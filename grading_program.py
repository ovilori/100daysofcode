#this program converts the scores of students to grades, and stores the name and grades in a new dictorinary.
#dictionary containing student's name and scores.
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#empty dictionary to store student's name and grades
student_grades = {}
#adding the grades to student_grades dictionary
for name, score in student_scores.items():
    if score > 90:
        student_grades[name] = "Outstanding"
    elif score > 80:
        student_grades[name] = "Exceeds Expectations"
    elif score > 70:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"
#print the student_grades dictionary
print(student_grades)
