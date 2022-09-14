def sum_of_total(n, a):
    ans = 0
    for i in range(n):
        ans += a[i]
    print("The sum of n number:", ans)

def sum_of_index(n, a):
    ans_1 = 0
    for i in range(1, n+1):
        ans_1 += i
    print("The sum of index:", ans_1)

def sum_using_formula(n, a):
    ans_2 = n*(n+1)/2
    print("The sum of index using formula:", ans_2)   

n = int(input("Enter the n number:"))
a = input().split()
for i in range(n):
    a[i] = int(a[i])
sum_of_total(n, a)
sum_of_index(n, a)
sum_using_formula(n, a)