import sys

sys.stdin = open("_직사각형길이찾기.txt")


from collections import Counter
tc=int(input())

for i in range(tc):
    length=Counter(list(map(int, input().split()))).most_common()
    if len(length) == 1 :
        print(f'#{i+1}',length[0][0])
    else :
        print(f'#{i+1}',length[1][0])



