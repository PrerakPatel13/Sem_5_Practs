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


def left_shift(A, Q):
    a = A[1:]
    a = a+Q[0]
    q = Q[1:]
    return a, q


def print_iter(a, q):
    print(f'Accumulator: {a}')
    print(f'MUltipier: {q}', end='\n\n')


Q = bin(int(input('Enter Dividend : ')))[2:]
M = bin(int(input('Enter Divisor : ')))[2:]

if(len(M) > len(Q)):
    Q = Q.zfill(len(M))
else:
    M = M.zfill(len(Q))

A, M = '0'*(len(M)+1), M.zfill(len(M)+1)
M_neg  = two_comp(M)

print_iter(A, Q)

for i in range(len(Q)):
    print('INteration: ',i)
    A, Q = left_shift(A, Q)
    print_iter(A, Q)
    A = add_bin(A, M_neg)
    print_iter(A, Q)
    if(A[0] == '0'):
        Q = Q+'1'
    else:
        Q = Q + '0'
        A  = add_bin(A, M)
    print_iter(A, Q)
    

rem  = int(A, 2)
quo = int(Q, 2)
print(f'Remainder is: {rem}')
print(f'Quotient is: {quo}')





