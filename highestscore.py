#This program calculates the highest score from a List of scores.
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
maximum_score = 0
for score in student_scores:
    if score > maximum_score:
        maximum_score = score
print(f'The highest score in the class is: {maximum_score}')
        




