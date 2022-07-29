import sys

sys.stdin = open("_문자열의거울상.txt")

tc=int(input())
for i in range(tc):
    word=input()
    word=word[::-1]
    result=''
    for j in word:
        if j == 'b':
            result+='d'
        if j == 'd':
            result+='b'
        if j == 'q':
            result+='p'
        if j == 'p':
            result+='q'
    print(f'#{i+1}',result)