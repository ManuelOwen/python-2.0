def addNumbers(a,b):
    try:
        c = a+b
        return c
    except Exception as e:
        
        print("invalid number")
        return e
    finally:
        print("Finally block executed")
        
print(addNumbers(2,3))
print(addNumbers(2,'3'))
print(addNumbers(2,4))