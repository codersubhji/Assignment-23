#2. Create a generator to produce first n odd natural numbers

def first_N_natural_genrate(x):
    num=1
    while num<=x:
        yield 2*num-1
        num+=1
        
for i in first_N_natural_genrate(10):
    print(i , end=" ")
    

    
