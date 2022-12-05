#8. Create an endless iterator using generator method to produce Prime numbers

def Endless_prime_number(num):
    for i in range(2,num):
        for e in range(2, i):
            if i%e==0:
                break
        else:
            yield e

for x in Endless_prime_number(10):
    print(x,end=" ")                
