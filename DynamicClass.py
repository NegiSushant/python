def choose_Class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo #return the class, not an instance
    else:
        class Bar(object):
            pass
        return Bar

MyClass = choose_Class('foo')
print(MyClass) #function returns a class, not an instance

print(MyClass()) #you can create an object from this class

print(type(1)) #<class 'int'>

print(type("1")) #<class 'str'>


myShinyClass = type('MyShinyClass', (), {}) #return a class object
print(myShinyClass)

print(myShinyClass()) #create an instance with the class
