import sys

sys.stdin = open("_신용카드만들기2.txt")
tc=int(input())
for i in range(tc):
    n=input()
    temp=n.split('-')
    if len(temp) ==  4 and len(n)-3 == 16 and temp[0][0] in '34569':
        print(f'#{i+1}', 1)
    elif len(temp) == 1 and len(n) == 16 and temp[0][0] in '34569':
        print(f'#{i+1}', 1)
    else : 
        print(f'#{i+1}', 0)
    
