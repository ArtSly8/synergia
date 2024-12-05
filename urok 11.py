
def fac(a):
    b = 1 
    for i in range (1,a+1):
        b*=i
    return b
spisok =[]
for a in range(6,0,-1):
    spisok.append(fac(a))
print(spisok)

    