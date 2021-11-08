class translator:
    def tran(self,y,i,v,x) :
        rom = ''
        if y==9:
            rom+=i+x
        elif y==4:
            rom+= i+v
        else :
            rom+=v*(y//5)+i*(y%5)
        return rom
    def deciToRoman(self, num):
        ans = ''
        ans+= self.tran(num//1000,'M','M','M')
        ans+= self.tran((num//100)%10,'C','D','M')
        ans+= self.tran((num//10)%10,'X','L','C')
        ans+= self.tran(num%10,'I','V','X')
        return ans
        ### Enter Your Code Here ###
    def romanToDeci(self, s):
        s = s.replace("XC",'h').replace("XL",'f').replace("IX",'n').replace("IX",'n').replace("CM",'t').replace("CD",'F').replace("IV",'4')
        return s.count('I')+s.count('V')*5 +s.count('n')*9 +s.count('f')*40 +s.count('h')*90 +s.count('X')*10 +s.count('F')*400+ s.count('t')*900 +s.count('M')*1000 +s.count('C')*100 +s.count('L')*50 +s.count('D')*500+s.count('4')*4
num = int(input("Enter number to translate : "))
if(num<=4999 and num>0):
    print(translator().deciToRoman(num))
    print(translator().romanToDeci(translator().deciToRoman(num)))

