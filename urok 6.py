a = int(input("Введите число: "))
nuley = 0
for i in range(a):
    b = int(input("Введите число: "))
    if b == 0:
        nuley += 1
print(nuley)

a = int(input("Введите число "))
c = 1
for i in range(1,a):
    if a % i == 0:
        c+=1
print(c)


a = int(input())
b = int(input())
for i in range(a,b):
    if i % 2 == 0:
        print(i, end=(" "))

