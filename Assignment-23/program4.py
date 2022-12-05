#4. Create a generator to produce squares of first N natural numbers
def square_first_natural(num):
    x=1
    while num>=x:
        yield x**2
        x+=1

for i in square_first_natural(10):
    print(i, end=" ")        