def armstrong(n):
    m = n
    tot = 0
    while n > 0:
        rem = n % 10
        tot += rem ** 3
        n = n // 10
    if tot == m:
        print("armstrong")
    else:
        print("not")

def armstrong_2(n):
    m = str(n)
    ans = 0
    for i in m:
        ans += int(i) ** 3
    if ans == n:
        print("armstrong")
    else:
        print("not")
        
n = int(input("Enter the number:"))
armstrong(n)
armstrong_2(n)