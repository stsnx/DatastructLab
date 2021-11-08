
sl = list()
bl = list()
ans = list()
def perket(idx, num, b, s):
    if(idx == len(n)):
        if(num != 0):
            ans.append(abs(b-s))
        return;
    ss = s * int(sl[idx])
    bb = b + int(bl[idx]) 
    perket(idx + 1, num, b, s)
    perket(idx + 1, num + 1, bb, ss)
    
n = input('Enter Input : ').split(',')
for i in n:
    s, b = i.split()
    sl.append(s) 
    bl.append(b)
sl.append(0) 
bl.append(0) 
perket(0, 0, 0, 1)
print(min(ans))

