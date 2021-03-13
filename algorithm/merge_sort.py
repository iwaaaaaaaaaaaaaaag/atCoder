# マージソートとは？
# 結構むずい
# 配列をどんどん分割していく
# 二つの配列を比較し、小さい方か入れていく

import random

def merge_sort(lists):
    # 分割できないなら値を返す
    if len(lists) <= 1:
        return lists

    # 分割できるなら再帰的に呼び出し
    center = len(lists) // 2
    left = lists[:center]     # ソート前
    right = lists[center:]    # ソート前
    left = merge_sort(left)   # ソート後
    right = merge_sort(right) # ソート後
    
    left_i = right_i = lists_i = 0
    while left_i < len(left) and right_i < len(right):
        if left[left_i] <= right[right_i]:
            lists[lists_i] = left[left_i]
            left_i += 1
        else:
            lists[lists_i] = right[right_i]
            right_i += 1
        lists_i += 1

    while left_i < len(left):
        lists[lists_i] = left[left_i]
        left_i += 1
        lists_i += 1        

    while right_i < len(right):
        lists[lists_i] = right[right_i]
        right_i += 1
        lists_i += 1    

    return lists

if __name__ == '__main__':
    nums = [random.randint(0,1000) for _ in range(10)]
    nums = [5,4,1,8,7,3,2,9,10]
    print(nums)
    print(merge_sort(nums))