# def solution(l):
#     print(5)

list = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]



#Breaking all strings into list
for i in range(0,len(list)):
    list[i] = list[i].split(".")
    

print(list)