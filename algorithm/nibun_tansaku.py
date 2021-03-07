search_list = list(range(100))

left_index = 0
right_index = len(search_list)

target = 70

i = 0
while True:
    i += 1
    middle_index = (left_index + right_index) // 2

    if search_list[middle_index] < target:
        left_index = middle_index
        continue
    elif search_list[middle_index] > target:
        right_index = middle_index
        continue
    elif search_list[middle_index] == target:
        print("count",i)
        break


    