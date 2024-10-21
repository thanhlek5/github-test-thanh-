def mergeTwoList(list1,list2):
    list3=[]
    for i in range(len(list1)):
        list3.append(list1[i])
    for j in range(len(list2)):
        list3.append(list2[j])
    for k in range(len(list3)):
        for t in range(k+1):
            if list3[k] < list3[t]:
                steep = list3[k]
                list3[k]=list3[t]
                list3[t]=steep            
    return list3
la = [1,2,4]
lb= [1,3,4]
print(mergeTwoList(la,lb))

