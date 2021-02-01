start_x, start_y, goal_x, goal_y = (int(x) for x in input().split())

# -(x - start_x) / (0 - start_y) = ( goal_x - x ) / (goal_y - 0)
x = (start_y * goal_x + goal_y * start_x)/(start_y + goal_y)
print(x)
