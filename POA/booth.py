def binary_conv(m,n):
    if(m>0 and n>0):
        a, b = bin(m)[2:], bin(n)[2:]
        i =  len(a) if len(a)>len(b) else len(b)
        return a.zfill(i+1), b.zfill(i+1)
    elif(m>0 and n<0):
        a, b = bin(m)[2:], bin(n)[3:]
        i =  len(a) if len(a)>len(b) else len(b)
        return a.zfill(i+1), b.zfill(i+1)
    elif(m<0 and n>0):
        a, b = bin(m)[3:], bin(n)[2:]
        i =  len(a) if len(a)>len(b) else len(b)
        return a.zfill(i+1), b.zfill(i+1)
    else:
        a, b = bin(m)[3:], bin(n)[3:]
        i =  len(a) if len(a)>len(b) else len(b)
        return a.zfill(i+1), b.zfill(i+1)
    

def add_bin(a, b):
    c = len(a)
    carry = '0'
    res = ''
    for i in range(c-1, -1, -1):
        if(a[i]=='1' and b[i]=='1' and carry=='1'):
            res = '1'+res
            carry = '1' 
        elif((a[i]=='1' and b[i]=='1' and carry=='0')or(a[i]=='1' and b[i]=='0' and carry=='1')or(a[i]=='0' and b[i]=='1' and carry=='1')):
            res = '0'+res
            carry = '1'
        elif((a[i]=='1' and b[i]=='0' and carry=='0')or(a[i]=='0' and b[i]=='1' and carry=='0')or(a[i]=='0' and b[i]=='0' and carry=='1')):
            res = '1'+res
            carry = '0'
        else:
            res = '0'+res
            carry = '0'
    
    return res
        

def two_comp(a):
    c = len(a)
    res =''
    for i in range(c):
        if(a[i] == '0'):
            res = res + '1'
        else:
            res = res + '0'
    one = '0'*(c-1)+'1'
    res = add_bin(res, one)
    return res


def right_shift(A, Q):
    q0  = Q[-1]
    c = len(Q)
    q, a = Q[:c-1], A[:c-1]
    q = A[-1]+Q
    a = A[0]+a
    return a[:c], q[:c], q0


def print_iter(a, q, q0):
    print(f'Accumulator: {a}')
    print(f'MUltipier: {q}')
    print(f'Storing bit: {q0}', end='\n\n')


a = int(input('Enter Multiplicand : '))
b = int(input('Enter Multiplier : '))

M, Q = binary_conv(a, b)



M_neg = two_comp(M)

print(f'Multiplier: {M}\nMultiplicand: {Q}\n -Multiplier: {M_neg}', end='\n\n')


A = '0'*len(M)
Q0 = '0'
print_iter(A, Q, Q0)
for i in range(len(M)):
    print(f'Iteration {i} :')
    if(Q[-1] == '0' and Q0 == '1'):
        A = add_bin(A, M)
        A, Q, Q0 = right_shift(A, Q)
    elif(Q[-1]=='1' and Q0 == '0'):
        A = add_bin(A, M_neg)
        A, Q, Q0 = right_shift(A, Q)
    else:
        A, Q, Q0 = right_shift(A, Q)
    print_iter(A, Q, Q0)

res = A+Q
print(f'The decimal answer is: {res}')
bool_check = (((a>0)and(b<0)) or ((a<0)and(b>0)))
if bool_check: # for negative number as output
    res= two_comp(res)
    ans = int(res,2)
    print(f'The result is: -{ans}')
else:
    ans = int(res,2)
    print(f'The result is: {ans}')












    
    
