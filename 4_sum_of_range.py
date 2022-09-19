def sum_range(s, a):
    tot = 0
    for i in range(s, e):
        tot += i
    return tot
s = int(input("Enter the Starting number:"))
e = int(input("Enter the ending number:"))
tot = sum_range(s, e)
print("The sum of range between {0} to {1} is:{2}".format(s, e, tot))