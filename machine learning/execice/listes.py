
def fibonacci(n):
    x = 0
    b = 1
    fib = [x]
    while x < n:
        print(x)
        x, b = b, x+b
        fib.append(x)
    return fib
    
    #retourner la suite de fibonaci jusqu'a une valeur n

fibonacci(1000)
