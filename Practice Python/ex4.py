number = int(input('give me nr:'))

divisors = [];

for x in range(1,number):
    
    if (number % x == 0):
        divisors.append(x)
        
print (divisors)