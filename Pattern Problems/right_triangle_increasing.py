#Print Right Angled Triangle(Increasing)
n = int(input("Enter Size:"))
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    print()

# Output
# Enter Size:5
# *
# * *
# * * *
# * * * *
# * * * * *