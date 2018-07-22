if __name__ == '__main__':
    N = int(input())
    newList = list()
    
    for _ in range(N):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd == "print":
            print(newList)
        else:
            cmd += "(" +",".join(args) + ")"
            eval("newList."+cmd)
    
    
    
#     N = int(input())    
#     tempList = list()
#     finalList = list()
    
#     for i in range(N):
#         tempList.append(input().split())
#         # if input() == "insert":
#         #     tempList.insert(input(),input())
#         # elif input() == "print":
    
    
    # for i in range(N):
    #     for j in range(0,len(tempList[i])):
    #         if(tempList[i][0]) == "print":
    #             # print("print function")
    #             eval(print(finalList))
    #         else:
    #             cmd = tempList[i][0]
    #             args = 0
    #             eval("finalList."+cmd+"("+ args +")")
            
                
# https://www.hackerrank.com/challenges/python-lists/forum