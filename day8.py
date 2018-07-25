n = int(input())
phone = {}

for _ in range(n):
    line = input().strip().split(" ") #this seems to be a common way to parse input in python
    phone.update({line[0]:line[1]})

for _ in range(n):
    if input() in phone.keys():
        print(input()+"="+phone[input()])
    else:
        print("Not found")
# print(phone["sam"])
