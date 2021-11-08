#-10, 66, -56, -9, -32, -41, 81, 10, 31, 65, -84, -73, -63, 94, -100, -56, -88, 41, 44, -45, -61, 12, 27, 85, -69, -26, -74, -18, -60, 90
#[-10, -84, -73, -63, -100, -56, -88, -45, -61, 12, 27, 85, 90]
def asteroid_collision(asts,i):
    if i>=len(asts)-1:
        ans = []
        #ans = [int(i) for i in asts if i!=0]
        ans = asts
        print(str(ans).replace(" 0,",'').replace("[0, ",'[').replace(", 0]",']').replace('[0]','[]'))
        return 0
    if asts[i]<0:
       # print('-')
        if asts[i-1]>=0 and i>0:
            if abs(asts[i])==asts[i-1]:
                asts[i-1] = 0
                asts[i]=0   
                asteroid_collision(asts,i-1)
            elif max(abs(asts[i]),asts[i-1])== abs(asts[i]):
              #  print('+- = -')
                asts[i-1] = asts[i]
                asts[i]=0
              #  print(str(i)+str(asts))
                asteroid_collision(asts,i-1)
            else :
              #  print('+- = +')
                asts[i] = asts[i-1]
                asts[i-1]=0
                #print(str(i)+str(asts))
                asteroid_collision(asts,i-1)
        else :
            asteroid_collision(asts,i+1) 
    elif asts[i]>0 and i<=len(asts)-1:
       # print('+')
        if asts[i+1]<=0:
            if abs(asts[i+1])==asts[i]:
                asts[i+1] = 0
                asts[i]=0
                asteroid_collision(asts,i+1)
            elif max(abs(asts[i+1]),asts[i])== asts[i]:
               # print('+- = +')
                asts[i+1] = asts[i]
                asts[i]=0
               # print(str(i)+str(asts))
                asteroid_collision(asts,i+1)

            else :
               # print('+- = -')
                asts[i] = asts[i+1]
                asts[i+1]=0
               # print(str(i)+str(asts))
                asteroid_collision(asts,i)
        else :
            asteroid_collision(asts,i+1) 
    elif asts[i]==0:
      #  print('0')
        if i<len(asts)-1:
         #   print(str(i)+"lrn")
          #  print(str(i)+str(asts))
            asteroid_collision(asts,i+1)       
        elif i>=len(asts) :
           # print(str(i)+"lrn+")
          #  print(str(asts))
            return 0
x = input("Enter Input : ").replace(', ',',').split(",")
x = list(map(int,x))
asteroid_collision(x,0)
