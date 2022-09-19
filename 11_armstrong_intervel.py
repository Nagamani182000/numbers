def armstrong_num(s, e):
    for i in range(s, e):
        m = i
        tot = 0
        while i > 0:
            rem = i % 10
            tot += rem ** 3
            i = i // 10
        if m == tot:
            print(tot, end=" ")

def armstrong_num_2(s, e):
    print("\n")
    for i in range(s, e):
        m = str(i)
        ans = 0
        for j in range(len(m)):
            ans += int(m[j]) ** 3
        if ans == i:
            print(ans, end=" ")

s = int(input("Enter the starting number:"))
e = int(input("Enter the ending number:"))
armstrong_num(s, e)
armstrong_num_2(s, e)