# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N, Stu = int(input()), input().split()
Student = namedtuple('Student', (c for c in Stu))
stud = []
total = 0
for i in range(N):
    student = input().split()
    stud.append(Student(student[0], student[1], student[2], student[3]))
    total = total + int(stud[i].MARKS)
print("{:.2f}".format(total/N))