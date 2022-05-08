student_heights = input("Input a list of student heights ").split()
# count = 0
# total_height = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
#   count += 1
# for i in range(0,count):
#     total_height += student_heights[i]
# print(total_height/count)
# print(student_heights)
total_height = sum(student_heights)
number_of_students = len(student_heights)
print(total_height/number_of_students)