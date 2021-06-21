#program to list no of item in dictionary and sort it with and without using function

y =[]
unsorted_list=[]
sorted_list=[]
d = {'shape':[1,2,4,5,6,8,9],'base': 65,"cube":68,"diameter":[4,5,7,8,0,9,2,1,]}
for i in d.keys():
    y.append(i)
    unsorted_list.append(i)
y.sort()          # by using inbuilt sort function
print("using function\n",y)

# sorting list without using function
while unsorted_list:
    minimum = unsorted_list[0]
    for j in unsorted_list:
        if j < minimum:
            minimum = j
    sorted_list.append(minimum)
    unsorted_list.remove(minimum)

print(sorted_list)