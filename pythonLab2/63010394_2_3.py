class TorKham:
	def __init__(self):

		self.words = []
	def restart(self):
            self.words = []
            if(self.words == []):
	            return 'game restarted'
	def play(self, word):
            if self.words == []:
                self.words.append(word)
                return f'\'{word}\' -> {self.words}'
            else :
                #print(self.words[len(self.words)-1][len(self.words[len(self.words)-1])-2:len(self.words[len(self.words)-1])].lower())
                #print(word[0:2].lower())
                if self.words[len(self.words)-1][len(self.words[len(self.words)-1])-2:len(self.words[len(self.words)-1])].lower()==word[0:2].lower() :
                        self.words.append(word)
                        return f'\'{word}\' -> {self.words}'  
                else :
	                    return f'\'{word}\' -> game over'
torkham = TorKham()
print("*** TorKham HanSaa ***")
S = input("Enter Input : ").split(',')
for x in S :
    ar = x.split(' ')
    if ar[0] == 'P' :
        print(torkham.play(ar[1]))
    elif ar[0] == 'R' :
        print(torkham.restart())
    elif ar[0] == 'X' :
        break
    else :
        print(f'\'{x}\' is Invalid Input !!!')
        break