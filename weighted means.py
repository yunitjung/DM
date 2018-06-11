list_array = []
list_weight = []
weighted=0
total_weight=0
weighted_means = 0

n = int(input())
input_array = input().split()
input_weight = input().split()

for i in input_array :
    list_array.append(int(i))
    
for i in input_weight :
    list_weight.append(int(i))
    
for i in range(len(list_array)):
    weighted+=(list_array[i]*list_weight[i])
    total_weight +=list_weight[i]

weighted_means = round(weighted/total_weight,1)
print(weighted_means)




    
