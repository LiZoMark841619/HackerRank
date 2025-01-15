from collections import namedtuple

while True:
    try:
        N = int(input('Enter the number of students: '))
        if N in range(1, 5):
            print(f'You have entered {N} students! ')
            break
        else:
            print('The number of students must be between 1 and 5! Try again! ')
    except ValueError:
        print('Invalid input! Try again! ')
    
column_names = input('Enter the column names: ').split()
Student = namedtuple('Student', column_names or 'ID MARKS NAME CLASS'.split())

marks = []
for _ in range(N):
    while True:
        values = input(f'Enter the data of the student #{_}: ').split()
        try:
            stu = Student(*values)
        except AttributeError:
            print('AttributeError! Try again with valid attributes! ')
        except TypeError:
            print('TypeError! Try again with valid inputs! ')
        except ValueError:
            print('ValueError! Try again with valid inputs! ')
        else:
            marks.append(stu.MARKS)
            break

total = sum(int(value) for value in marks)
print(total/N)