dic = {}

print("Enter number of friend want to add: ")
num = int(input())

for i in range(0,num):
    print("Enter name: ")
    name = input()
    if name not in dic:
        print("Enter birthday: ")
        dob = input()
        dic[name] = dob
    else:
        print("Sorry name already present: ")
print(dic)