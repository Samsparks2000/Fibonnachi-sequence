#fibbonachi sequence, 0 and 1 are constants
import math
seq = int(input("select how long you want the fibonacci seq to be: "))

def fib(n):
    x = [0, 1]
    for i in range(n):
        y = x[len(x) - 1] + x[len(x) - 2]
        x.append(y)
    return x


print(f"{fib(seq)}")




