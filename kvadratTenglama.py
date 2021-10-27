# Kvadrat tenglama
print("Assalomu alaykum\nBu kvadrat tenglamaning ildizlarini topib beradigan dastur!\nax^2 + bx + c = 0")
a = int(input("Iltimos a ni kiriting: "))
b = int(input("Iltimos b ni kiriting: "))
c = int(input("Iltimos c ni kiriting: "))
diskriminant = b ** 2 - 4 * a * c
if(diskriminant <= 0):
    print("Tenglama ildizga ega emas!")
elif(diskriminant == 0):
    x1 = (-b + (diskriminant ** 0.5)) / (2 * a)
    print("x1 va x2 = {}".format(x1))
else:
    x1 = (-b + (diskriminant ** 0.5)) / (2 * a)
    x2 = (-b - (diskriminant ** 0.5)) / (2 * a)
    print("x1 = {} va x2 {}".format(x1,x2))
