#Print Hill Pattern

n = int(input("Enter Size:"))
for i in range(n):
    for j in range(i,n):
        print(' ', end='')
    for j in range(i+1):
        print('*', end=' ')
    print()

# Output
# Enter Size:5
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *