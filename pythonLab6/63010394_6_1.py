def print1ton(n):
    if n>1:
        print1ton(n-1)
        print(n,end=' ')
    else :
        print('1',end=' ')
def printnto1(n):
    if n>1:
        print(n,end=' ')
        printnto1(n-1)
    else :
        print('1',end=' ')

n = int(input("Enter Input : "))

print1ton(n)
printnto1(n)