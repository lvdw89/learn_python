class Dog:
    
    kind ='canine'
    
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
    
d = Dog('Fido')

e = Dog('Buddy')

print(d.kind)