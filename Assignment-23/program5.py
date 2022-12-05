#5. Create a generator to produce first n terms of Fibonacci series

def febonacci_series(num):
    x,y,a=0,1,0
    while num>=a:
        yield x
        x,y=y,x+y
        a+=1
        
for i in febonacci_series(10):
    print(i , end=" ")