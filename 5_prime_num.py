def prime(n):
    for i in range(2, n):
        if n % i == 0:
            print("Not")
            break
    else:
        print("prime")
n = int(input("Enter the number:"))
prime(n)