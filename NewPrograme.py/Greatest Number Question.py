a = int(input("Enter First Number = "))
b = int(input("Enter Second Number = "))
c = int(input("Enter Third Number = "))
d = int(input("Enter Fourth Number = "))
if a >= b and a >= c and a >= d:
    print("First Number Is Largest >> ", a)
elif b > c and b > d:
    print("Second Number Is Largest >> ", b)
elif c > d:
    print("Third Number Is Largest >>", c)
else:
    print("Fourth Number Is Largest >>", d)
