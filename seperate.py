i = int(input('Enter the number'))

lst = []
for j in range(i):
    temp = input()
    lst.append(temp)

numblst = []
wordlst = []
for j in lst:
    temp = j.split()
    numblst.append(temp[0])
    wordlst.append(temp[1])

for j in numblst:
    print(j)

print()

for j in wordlst:
    print(j)
