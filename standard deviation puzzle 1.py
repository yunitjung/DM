
import math

def count_std(lst):
    m = sum(lst)/len(lst)
    total = [(i-m) ** 2 for i in lst]
    std = math.sqrt(sum(total)/len(total))
    return std

list_1 = [1,2,3]
std1 = count_std(list_1)

flag = True
N = 3
while flag :
    std2 = count_std(list_1+[N])
    if round(std2,3) == round(std1,3):
        print(round(N,2))
        flag = False
    N-=0.01
