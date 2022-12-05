"""7. Create an endless iterator using generator method to produce terms of Fibonacci
series"""

def Endeless_generate_feb(num):
    x,y,z=0,1,0
    while num>=z:
        yield x
        z+=1
        x,y=y,x+y
        
for i  in Endeless_generate_feb(10):
    print(i,end=" ")