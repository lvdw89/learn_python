import random

a = random.randint(1,10)

b = int(input('guess nr:'))

if (b>a):
    print('too high')
elif (b<a):
    print('too low')
else:
    print('ok')
        
