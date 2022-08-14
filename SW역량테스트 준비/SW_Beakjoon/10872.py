def factorial(n, sum):
    if n == 0:
        print(sum)
    else:
        sum = sum * n
        factorial(n-1,sum)


num = int(input())
sum = 1
factorial(num, sum)