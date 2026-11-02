
# Non-recursive Fibonacci program

n = int(input("Enter the number of terms: "))

a, b = 0, 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Recursive Fibonacci program

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the number of terms: "))

print("Fibonacci Series:")

for i in range(n):
    print(fibonacci(i), end=" ")

