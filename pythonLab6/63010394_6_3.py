def euclid(a,b):
    if a%b==0 : 
        return int(b)
    else : 
        return(euclid(b,a%b))
x,y = map(int,input('Enter Input : ').split())

if x==0 and y==0:
    print("Error! must be not all zero.")
else :
    an  = abs(euclid(x,y))
    if abs(x)<abs(y) and x!=0:
        t=y
        y=x
        x=t
    if x<y and x==0:
        t=y
        y=x
        x=t
    print(f'The gcd of {x} and {y} is : {an}')