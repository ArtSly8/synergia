a = input("Введите слово:")
if a==a[::-1]:
    print("yes")
else:
    print("no")

a = input()
b = " ".join(a.split())
print(b)