number=[1,2,3,4,5,6,7]

for a in number:
    b=a*10
    print(b)

number7=[1,2,3,4,5,6,7,8,9]

for a7 in number7:
    b7=a7*7
    print(b7)


for i in number7:
    print('4*',i,'=',i*7)

dan=[2,3,4,5,6,7,8,9]
for i in dan:
    if i==3:
        continue
    for j in number7:
        print(i,'*',j,"=",i*j)


