# クイックソートとは？
# 結構むずい　パーティションを決めてソートする
## パーティションを決める処理
## low と highの中でループ処理
## pivotをhighに値を設定
## jについてループ
## j <= high の場合
## i++
## jとiの値を入れ替え
## 処理の最後に highと i + 1と入れ替える（iまでがpivotよりも値が小さい、i+1以降がpivotよりも値が大きい）

## 繰り返して処理をする
## low からpartition - 1とpartition + 1からhigh 

import random

def execute_pertition(lists,low,high):
    pivot = lists[high] 
    i = low - 1
    for j in range(low,high):
        if lists[j] <= pivot:
            i += 1
            lists[i],lists[j] = lists[j],lists[i]
    
    # パーティションに使った値を適切な位置に挿入する
    lists[i + 1],lists[high] = lists[high],lists[i + 1]
    return i + 1

def quick_sort(lists,low,high):
    if low < high:
        pertition_index = execute_pertition(lists,low,high)
        quick_sort(lists,low,pertition_index - 1)
        quick_sort(lists,pertition_index + 1,high)
    return lists

if __name__ == '__main__':
    nums = [random.randint(0,1000) for _ in range(10)]
    print(nums)
    print(quick_sort(nums,0,len(nums) - 1))