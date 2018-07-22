# a[::2] will retrieve all array items (since it does not set up any from or to, and set the "pace"), starting from index 0, incrementing the index two by two and accessing all even indexes (0,2,4,6, and so on).
# s[1::2] will retrieve all array items, from index 1, incrementing the index two by two and accessing all odd indexes (1,3,5,7,9, and so on).


# https://www.hackerrank.com/challenges/30-review-loop/forum


for N in range(int(input())):
    S = input()
    print(S[::2], S[1::2])


# n = int(input())
# wordList = list()
# tempList = list()

# for _ in range(n):
#     wordList.append(input())

# print(wordList)

# for index in range(n): #goes through each word and add into list
#     tempList = list(wordList[index])
#     # print(tempList)
#     for j in range(len(tempList)):
#         if j%2:
#             print(tempList[j],end="")
#     print("\n")