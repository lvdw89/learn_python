#===============================================================================
# x = int (input('please enter an integer:'))
# 
# if x > 5 :
#     print (x)
#     
# elif x==4:
#  print ('blabla')
# 
# else:
#     print(5)
#===============================================================================


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def my_function():
    
     """Do nothing, but document it.
...
...     No, really, it doesn't do anything.
...     """
     pass

print (my_function.__doc__)