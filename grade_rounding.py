def gradingStudents(grades):
    final_grades = []
    for grade in grades:
        if grade <= 37 or grade % 5 == 0:
            final_grades.append(grade)
        elif grade % 5 != 0:
            counter = grade
            while counter % 5 != 0:
                counter += 1
            result = counter - grade
            if result < 3:
                grade = counter
            final_grades.append(grade)
    return final_grades
                
if __name__ == '__main__':
    grades = [int(input().strip()) for _ in range(int(input().strip()))]
    result = gradingStudents(grades)
    print(*result, sep='\n')