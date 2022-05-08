student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
maxi = student_scores[0]
for i in range(1,len(student_scores)):
    if  student_scores[i] > maxi:
        maxi = student_scores[i]
print(maxi)
# OR
print(max(student_scores))
print(min(student_scores))