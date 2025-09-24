# Program to create a square pattern of asterisks
# Size of the square (number of rows and columns)

n = 5 # if want custom size use n = int(input('Enter Size:'))
# Outer loop - controls the number of rows
for i in range(n):
    # Inner loop - controls the number of columns in each row
    for j in range(n):
        # Print an asterisk followed by a space
        # end=' ' prevents automatic newline
        print("*", end=' ')
    # After printing all asterisks in a row,
    # move cursor to the next line
    print()

# Expected output:
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *