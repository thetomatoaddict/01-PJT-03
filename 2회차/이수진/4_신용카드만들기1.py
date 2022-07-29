import sys

sys.stdin = open("_신용카드만들기1.txt")
tc = int(input())

for i in range(tc):
    nums=list(map(int, input().split()))
    result=0
    for j in range(15):
        if j%2 == 0 :
            result+=nums[j]*2
        elif j%2 != 0 :
            result+=nums[j]
 
    N=((result//10)*10)+10-result
    if N > 9:
        N=0
    print(f'#{i+1}',N)
