def polin(n):
    m = n
    tot = 0
    while n > 0:
        rem = n % 10
        tot = tot * 10 + rem
        n = n // 10
    if m == tot:
        print("polin")
    else:
        print("not")

def polin_2(n):
    m = str(n)
    ans = ""
    for i in range(len(m)-1, -1, -1):
        ans += m[i]
    if n == int(ans):
        print("polin")
    else:
        print("not")

n = int(input("Enter the number:"))
polin(n)
polin_2(n)