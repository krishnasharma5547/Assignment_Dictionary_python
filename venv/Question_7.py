# creating empty list
L1 = list()
L2 = list()

# creating empty dictionary
dic = {}

# input from user
print("Enter number of details you want to add: ")
num = int(input())
for i in range(num):
    L1.append(input())

for i in L1:
    L2.append(len(i))

# Adding element to dictionary
for i in range(num):
    dic[L1[i]] = L2[i]

# printing dictionary
print(dic)