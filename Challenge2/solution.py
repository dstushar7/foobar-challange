 def solution(l):
    result = sorted(l, key=lambda x:[int(i) for i in x.split('.')])
    return result


# #Breaking all strings into list
# for i in range(0,len(list)):
#     list[i] = list[i].split(".")


# for i in list:
#     for e in range(0,3):
#         try:
#             i[e] = int(i[e])
#         except:
#             i.append(-1)


# sortedINT = sorted(list, key=lambda x:x[0])
# print(sortedINT)



# for i in range(0,len(sortedINT)):
#     print(sortedINT)
#     if sortedINT[i+1]: #If array is not out of bounds
#         if sortedINT[i][0] == sortedINT[i+1][0]:#If there exists same elevator version to compare to
#             if sortedINT[i+1][1]:#If the latter elevator version point exists
#                 if sortedINT[i][1]>sortedINT[i+1][1]:
#                     temp = sortedINT[i]
#                     sortedINT[i] = sortedINT[i+1]
#                     sortedINT[i+1] = temp
#             else:
#                 if sortedINT[i][1]:
#                     temp = sortedINT[i]
#                     sortedINT[i] = sortedINT[i+1]
#                     sortedINT[i+1] = temp

