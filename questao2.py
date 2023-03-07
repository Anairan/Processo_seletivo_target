def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib

num = int(input("Digite um número: "))
fib = fibonacci(num)
if num in fib:
    print(f"O número {num} está na sequência de Fibonacci!")
else:
    if (num == 0):
        print(f"O número {num} está na sequencia de Fibonacci")
    elif (num == 1):
        print(f"O número {num} está na sequencia de Fibonacci")
    else:
        print(f"O número {num} não está na sequência de Fibonacci!")
