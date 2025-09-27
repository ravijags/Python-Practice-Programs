#Print Right Angled Triangle(Decreasing)

n = int(input("Enter Size:"))
for i in range(n):
    for j in range(i,n):
        print("*", end=' ')
    print()


# Output
# Enter Size:5
# * * * * * 
# * * * *
# * * *
# * *
# *