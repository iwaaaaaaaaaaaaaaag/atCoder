# セレクションソートとは？
# 一番最初のインデックスと値を保持する
# 保持している値よりも小さい値があれば、インデックスと値を書き換える
# 一番最初と保持した値を入れ替える
# 左の範囲を狭めてループする
import random

def selection_sort(lists):
    for i in range(len(lists) - 1): 
        tmp_index = i
        for j in range(i,len(lists)):
            if lists[tmp_index] > lists[j]:
                tmp_index = j
        lists[i],lists[tmp_index] = lists[tmp_index],lists[i] 
            

    return lists

if __name__ == '__main__':
    nums = [random.randint(0,1000) for _ in range(10)]
    print(nums)
    print(selection_sort(nums))