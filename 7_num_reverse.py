def reverse_num(n):
    tot = 0
    while n > 0:
        rem = n % 10
        tot = tot * 10 + rem
        n = n // 10
    print("The reverse number :", tot)

def reverse_num_2(n):
    m = str(n)
    for i in range(len(m)-1, -1, -1):
        print(m[i],end="")

n = int(input("Enter the number:"))
reverse_num(n)
reverse_num_2(n)