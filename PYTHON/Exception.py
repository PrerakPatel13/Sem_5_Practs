import time
print("\nKey Error implemenation")
try:
    dic = {'1':'params','2':'query'}
    print(dic['3'])
except KeyError as ke:
    print('Key error exception : ',ke)

print("\nimport error implemenation")   
try:
    import nonexistent_module
except ImportError:
    print("Import error: The module does not exist or cannot be imported.")  

print("\nzero Division Error implemenation")   
try:
    print(9/0)
except ZeroDivisionError as e:
    print(e)      

print("\nout range error handling implemenation")
try:
    l = []
    print(l[1])
except Exception as e:
    print(e)

print('\nkeyboard interrupt ')
try:
    print(input("Enter something : "))
    while True:
        print('print')
        time.sleep(1)
except Exception as kbe:
    print(kbe)    


class BaseError(Exception):pass
class HighValueError(Exception):pass
class LowValueError(Exception):pass
value = 81
while(1):
    try:
        n=int(input("Enter number:"))
        if n>value:
            raise HighValueError
        elif n < value:
            raise LowValueError
        else:
            print("Nice!Correct answer")
            break
    except LowValueError:
        print("Very Low Value, Give input again")
        print()
    except HighValueError:
        print("Very High value , give input again")
        print()    