# インサーションソートとは？
# 値の入れ替えはバブルソートと似ている
# インサーションソートは一気に適切な位置まで持っていく
import random

def insertion_sort(lists):
    for i in range(1,len(lists)): 
        
        j = i - 1
        while j >= 0:
            if lists[j] > lists[j + 1]:
                lists[j],lists[j + 1] = lists[j + 1],lists[j] 
            j -= 1
            

    return lists

if __name__ == '__main__':
    nums = [random.randint(0,1000) for _ in range(10)]
    print(nums)
    print(insertion_sort(nums))