import sys

sys.stdin = open("_최빈수구하기.txt")

from collections import Counter
tc = int(input())
for i in range(tc):
    case=int(input())
    scores=list(map(int, input().split()))
    scores=Counter(scores).most_common()
    result=[]
    for j in scores:
        if j[1]==scores[0][1]:
                result.append(j[0])
    print(f'#{i+1} {max(result)}')
    

