def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n - 1) + fibo(n - 2))


# the numbers we want to display


n_terms = 20

# check if the number of terms is valid
if n_terms <= 0:

    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(n_terms):
        print(fibo(i), end="   ")