from  collections import Counter  

H, W = map(int,input().split())
S_list = [list((map(str,input()))) for _ in range(H)]

# 角を数える
# 四つの範囲の中で、白３黒１　または白１黒３

ans = 0
for i in range(1,H):
    for j in range(1,W):
      tmp = Counter([S_list[i - 1][j - 1], S_list[i][j - 1], S_list[i - 1][j], S_list[i][j]])
      if tmp == Counter({'.': 3, '#': 1}) or tmp == Counter({'.': 1, '#': 3}):
          ans += 1
print(ans) 
