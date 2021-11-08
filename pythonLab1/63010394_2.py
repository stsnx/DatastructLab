print(" *** Wind classification ***")
s = input("Enter wind speed (km/h) : ")
s = float(s)
if s>= 209.0:
    print("Wind classification is Super Typhoon.")
elif s>= 102.0:
    print("Wind classification is Typhoon.")
elif s>= 56.0:
    print("Wind classification is Tropical Storm.")
elif s>= 52.0:
    print("Wind classification is Depression.")
else :
    print("Wind classification is Breeze.")