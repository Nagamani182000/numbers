def position(n):
    if n >= 0:
        if n > 0:
            pos = 1
        else:
            pos = 0
    else:
        pos = 2
    return pos
n = int(input("Enter the number:"))
pos = position(n)
if pos == 1:
    print("Positive number")
elif pos == 0:
    print("It is Zero")
else:
    print("Negative number")