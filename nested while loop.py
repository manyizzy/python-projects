# where a user enter a number and it becomes the number of rows

n = int(input("Enter a number "))
i = 1
while i <= n :
    j = 1
    while j <= i :
        print(i, end='')
        j += 1
    i += 1
    print()