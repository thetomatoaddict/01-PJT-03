import sys

sys.stdin = open("_소득불균형.txt")

tc=int(input())

for i in range(tc):
    n=int(input())
    nums=list(map(int, input().split()))
    avg=sum(nums)/n
    result=0
    for j in nums:
        if j <= avg:
            result+=1
    print(f'#{i+1}',result)

