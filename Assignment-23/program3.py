#3. Create a generator to produce first n even natural numbers

def Even_n_naturalNumber(num):
    x=1
    while num>=x:
        yield 2*x
        x+=1

for i in Even_n_naturalNumber(10):
    print(i,end=" ")  
      