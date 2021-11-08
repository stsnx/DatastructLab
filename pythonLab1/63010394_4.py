def odd_list(alist):
    a = [i for i in alist if i%2==1]
    return a

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)
