#위치인자
def get_sum(a,b):
    result=a+b
    return result

#n1=get_sum(10,20)
#print('10과 20의 합 =',n1)

#n2=get_sum(100,200)
#print('100과 200의 합=',n2)


#키워드인자
def get_sum_1(a=1, b=2):
    result=a+b
    return result


n3=get_sum_1()
print(n3)

def get_sum_2(a=1, b=2,c=3,d ):
    result_1 = a+b
    result_2 = c-d
    return result_1, result_2

n4=get get_sum_2(5,6)
print(n4)



