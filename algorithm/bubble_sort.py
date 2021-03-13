# バブルソートとは？
# i i+1で値を比較し、大きい順に並べる
# 見る範囲をどんどん狭めていく

def bubble_sort(lists):
    for i in range(len(lists) - 1): 
        for j in range(len(lists) - (i + 1) ):
            if lists[j] > lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]

    return lists

if __name__ == '__main__':
    nums = [2,5,1,8,7,3]
    print(bubble_sort(nums))