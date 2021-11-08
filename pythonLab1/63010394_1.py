print("*** Converting hh.mm.ss to seconds ***")
h,m,s = map(int,input("Enter hh mm ss : ").split())
if m<60 and m>=0 and s>=0 and s<60: 
    print(f'{h:02d}:{m:02d}:{s:02d} = {h*3600+m*60+s:,} seconds')
elif m>=60 or m<0:
    print("mm("+str(m)+") is invalid!")