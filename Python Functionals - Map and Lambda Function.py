cube = lambda x: x**3

def fibonacci(n):
    fib = [0, 1]
    if n == 0:
        fib = []
    elif n == 1:
        fib = [0]
    elif n > 2:
        for i in range(2, n):
            fib.append(fib[i-2] + fib[i-1])
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# Sample Input
# 5
# Sample Output
# [0, 1, 1, 8, 27]

