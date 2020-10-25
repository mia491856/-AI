a1=int(input("a"))
b1=int(input("b"))
c1=int(input("c"))

def root_ex(a,b,c):
    x1 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    print('해는',x1,'또는',x2)

root_ex(a1,b1,c1)