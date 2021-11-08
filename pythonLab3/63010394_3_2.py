
def ManageStack(list):
    d = []
    for i in list :
        temp = i.split(" ")
        if temp[0] == 'A' :
            d.append(int(temp[1]))
            print("Add = "+temp[1])
        elif temp[0] == 'P' :
            if(len(d)==0) :
                print("-1") 
            else : 
                print("Pop = "+str(d[len(d)-1])) 
                d.pop(len(d)-1)
        elif temp[0] == 'D' :
            t = []
            if(len(d)==0) :
                    print("-1") 
            else : 
                for j in range(len(d)-1,-1,-1) :
                    if d[j] != int(temp[1]) :
                        t.append(d[j])  
                    else : 
                        print("Delete = "+str(d[j]))
            t.reverse()      
            d = t   
        elif temp[0] == 'LD' :
            t = []
            if(len(d)==0) :
                    print("-1") 
            else : 
                for j in range(len(d)-1,-1,-1) :
                    if d[j] >= int(temp[1]) :
                        t.append(d[j])  
                    else : 
                        print("Delete = "+str(d[j])+" Because "+ str(d[j]) +" is less than "+temp[1])   
            t.reverse()     
            d = t   
        elif temp[0] == 'MD' :
            t = []
            if(len(d)==0) :
                    print("-1") 
            else : 
                for j in range(len(d)-1,-1,-1) :
                    if d[j] <= int(temp[1]) :
                        t.append(d[j])  
                    else : 
                        print("Delete = "+str(d[j])+" Because "+ str(d[j]) +" is more than "+temp[1])   
            t.reverse()     
            d = t 
    return d                         
list = [x for x in input("Enter Input : ").split(",")]
y = ManageStack(list)
print ("Value in Stack = "+str(y))