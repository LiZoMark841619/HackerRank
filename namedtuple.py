from collections import namedtuple

N = int(input())
column_names = input().split()
Student = namedtuple('Student', column_names)

marks = []
for _ in range(N):
    stu = Student(*input().split())
    marks.append(stu.MARKS)

total = 0
for value in marks:
    total += int(value)

print(total/N)