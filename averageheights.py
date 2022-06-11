#this program calculates the average student height from a list of heights.
#sets the sum of heights to zero
sum_of_heights = 0
#sets the number of students to zero
number_of_students = 0
#accepts user input and store in a list sing the split function
student_heights = input("Input a list of student heights: ").split()
#iterate over the list to convert each height in the list to an integer
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  #increase the number of students by 1 after each iteration
  number_of_students += 1
  #calculate the sum of the heights
  sum_of_heights += student_heights[n]
#calculate the average height
average_height = round(sum_of_heights / number_of_students)
#print out the number of students, sum of students and the average height
print(f'Total number of students: {number_of_students}')
print(f'Sum of height of the students: {sum_of_heights}')
print(f'The average height of the students: {average_height}')


