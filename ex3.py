# write a factorial function, given n, you return n!
def factorial(n):
    number = 1
    product = n
    while number <= (n - 1):
        product = product * (n-number)
        number = number + 1 
    return product

print(factorial(3))

        


