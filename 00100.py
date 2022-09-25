int_a,int_b=map(int,input().split())
list_1=list()
if int_a>int_b:
    int_a,int_b=int_b,int_a
for i in range(int_a,int_b+1):
    list_1.append(i)
    int_a,int_b=int_b,int_a
def num(i):
    list_2=[]
    list_2.append(i)
    while 1 not in list_2:
            if i%2==0:
                list_2.append(int(i/2))
                i=i/2
            else:
                list_2.append(int(3*i+1))
                i=3*i+1
    list_2.sort()
    return len(list_2)
list_3=list()    
for i in list_1:
    num(i)
    list_3.append(num(i))
print(str(int_a),str(int_b),str(max(list_3)))