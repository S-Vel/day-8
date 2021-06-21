#program to find the repeated elements in list

a_sh = ["a","c","s","f","r","s","c","h","a","b","g","h"]
b_sh = []
c_sh = []
for i in a_sh:
    if i not in b_sh:
        b_sh.append(i)
    elif i not in c_sh:
        c_sh.append(i)
    else:
        None
print("the repeated charaters are:", c_sh )
