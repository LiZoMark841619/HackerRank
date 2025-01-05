def gradingStudents(grade: int) -> int:
    if grade > 37 and grade % 5 != 0:
        counter = grade
        while counter % 5 != 0:
            counter += 1
        result = counter - grade
        if result < 3:
            return counter
    return grade
                
if __name__ == '__main__':
    n = 0
    while n not in range(1, 61):
        n += int(input())
        
    for _ in range(n):
        grade = int(input())
        print(gradingStudents(grade))