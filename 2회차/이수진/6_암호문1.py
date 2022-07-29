import sys

sys.stdin = open("_암호문1.txt")
for i in range(10):
    secured_code_len =int(input())
    secured_code = list(map(int, input().split()))
    command_n = int(input())
    commands = list(map(str, input().split('I')))
    for j in range(1,command_n+1):
        temp=commands[j].split()
        for k in temp[int(temp[1])+1:1:-1]:
            secured_code.insert(int(temp[0]), k)
        
    print(f'#{i+1}',*secured_code[0:10])
