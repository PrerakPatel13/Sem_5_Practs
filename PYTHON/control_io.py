a=int(input("Enter a number:"))
print("square root of number:",a**0.5)

l,b= int(input("enter length:")),int(input("enter breadth:"))
print("Perimeter",2*(l+b),"area:",l*b)

a,b= int(input("enter 1st number:")),int(input("enter 2nd number:"))
c=a
a=b
b=c
print("Numbers after swap 1st:",a,"2nd:",b)

a,b= int(input("enter 1st number:")),int(input("enter 2nd number:"))
a,b=b,a
print("Numbers after swap 1st:",a,"2nd:",b)

a,b = int(input("Enter 1st numbers : ")), int(input("Enter 2nd numbers : "))
print("a :",a," b :",b)
a = a+b 
b = a-b
a = a-b
print("After Swapping ")
print("a:",a,"b:",b)

n= int(input("Enter size of set:"))
s=set()
for i in range(n):
    s.add(int(input(f'Enter element {i}:')))
print("Set: ",s)    

n= int(input("Enter size of list:"))
l=list()
for i in range(n):
    l.append(int(input(f'Enter element {i}:')))
print("List: ",l)    


n= int(input("Enter size of tuple:"))
t=tuple()
l=list(t)
for i in range(n):
    l.append(int(input(f'Enter element {i}:')))
t=tuple(l)
print("Tuple: ",t)    


n= int(input("Enter size of pattern:"))
for i in range(1,n+1):
    for j in range(1,j+1):
        print(i,end=" ")
    print()    

n= int(input("Enter size of pattern:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()    
    
n= int(input("Enter Number:"))
fact=1
if(n<0):
    print("Negative numbers ka factorial nai hota")
elif(n==0):
    print('Fact of 0 is 1')
else:
    for i in range(1,n+1):
        fact=fact*i
    print('Factorial:',fact)    

n= int(input("Enter Number:"))
fact=1
if(n<0):
    print("Negative numbers ka factorial nai hota")
elif(n==0):
    print('Fact of 0 is 1')
else:
    while(n>0):
        fact=fact*n
        n=n-1
    print('Factorial:',fact)     

n= int(input("Enter series size:"))
a=0
b=1
if(n<=0):
    print("valid input de ")
else:
    print(a,b,end=" ")
    for i in range(2,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c

n= int(input("Enter number:"))
if(n%2==0):
    print("Even")
else:
    print("odd")    

year= int(input("Enter year:"))
if(year%4==0):
    if(year%100!=0):
        print("Leap Year ")
    else:
        if(year%400==0):
            print("Leap Year")  
        else:
            print("Not a leap year")     
else:
    print("Not a leap year")  

num=4.0
if(type(num)==int):
    print("Integer")
elif(type(num)==float):
    print("Float")    
elif(type(num)==str):
    print("String")
elif(type(num)==list):
    print("List")  
elif(type(num)==tuple):
    print("Tuple")
elif(type(num)==set):
    print("Set")
else:
    print("Complex")     

print("\nbreak continue pass example : ")
for letter in 'python':
    if letter == 't' or letter == '0':
        continue
    print('current letter:',letter)
print()
for letter in 'python':
    if letter == 'y':
        break
    print('current letter:',letter)
print()
for letter in 'python':
    if letter in ['p', 'y', 't', 'h']:
        print('hi')
        pass
    print('pass letter:',letter)               


    