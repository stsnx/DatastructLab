print("*** Reading E-Book ***")
s,h = input("Text , Highlight : ").split(",")
print(s.replace(h,f'[{h}]'))