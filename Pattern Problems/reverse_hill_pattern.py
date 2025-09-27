#Print Reverse Hill Pattern

n = int(input('Enter Size:'))
for i in range(n):
    for j in range(i):
        print('',end=' ')
    for j in range(i,n):
        print('*', end=' ')
    print()