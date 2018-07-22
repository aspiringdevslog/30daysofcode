if __name__ == '__main__':
    
    min = 999
    studentList = list()
    secondLow = 999
    secondLowList = list()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        if score < min:
            studentList.insert(0,[name,score])
            min = score
        else:
            studentList.append([name,score])
            
    # print(len(studentList))
    # print(studentList[0][0])
    
    #some way to loop through the student list and remove the lowest score student, hence the new lowest score would be the 2nd min
    
    for i in range(len(studentList)):
        if studentList[i][1] != min and studentList[i][1] < secondLow:
            secondLow = studentList[i][1]
            # print(studentList[i][1])

    for i in range(len(studentList)):
        if studentList[i][1] == secondLow:
            secondLowList.append(studentList[i][0])
    
    secondLowList.sort()
    
    for student in secondLowList:
        print(student)
        
    