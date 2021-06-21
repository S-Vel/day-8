#program to find mean ,median,mode
#mean

lst_1=[2,3,3]                                                   # three given numbers
lst2 = lst_1
addi = 0
for q in lst_1:
    addi = addi +q
#print("addition",addi)
lenngth = len(lst_1)
mean = addi /lenngth
print("mean:",mean)


#median
lst2.sort()
n = len(lst2)
if n % 2 ==0:
    median1 = lst2[n//2]
    median2 = lst2[n//2-1]
    median = (median1+median2)/2
else:
    median = lst2[n // 2]
print("median is:"  + str(median))


#mode
yia = lst_1
yia.sort()
l1=[]

i = 0
while i < len(yia):
    l1.append(yia.count(yia[i]))
    i += 1

dia1 = dict(zip(yia , l1))

dia2 = {k for (k,v) in dia1.items() if v== max(l1)}

print("Mode is/are:" + str(dia2))