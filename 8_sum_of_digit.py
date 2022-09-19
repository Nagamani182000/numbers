def sum_digit(n):
    tot = 0
    while n > 0:
        rem = n % 10
        tot += rem
        n = n // 10
    print("The sum of digit:", tot)

def sum_digit_2(n):
    ans = 0
    m = str(n)
    for i in m:
        ans += int(i)
    print("The sum of digit:", ans)

n = int(input("Enter the number:"))
sum_digit(n)
sum_digit_2(n)