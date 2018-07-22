if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        # print(name)
        # print(*line)
        scores = list(map(float, line))
        # print(scores)
        student_marks[name] = scores
        # print(student_marks[name])
    query_name = input()
    
    newScore = sum(student_marks[query_name]) / len(student_marks[query_name]) 
    print(format(newScore, '.2f'))