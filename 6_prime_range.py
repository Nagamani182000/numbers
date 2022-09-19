def prime(s, e):
    for i in range(s, e+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=" ")
s = int(input("Enter the starting number:"))
e = int(input("Enter the ending number:"))
prime(s, e)