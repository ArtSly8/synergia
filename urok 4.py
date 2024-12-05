a = float(input("введите сторону a: "))
b = float(input("введите сторону b: "))
S = round(a * b, 2)
P = a + b
print(f'Площадь равна {S},Периметр равен {P}')

a,b,c,d,e = map(int, input("Введите через пробел каждую цифру пятизначного числа: ").split())
step1 = d**e
step2 = step1*c
step3 = a-b
step4 = step2 / step3
print(step4)