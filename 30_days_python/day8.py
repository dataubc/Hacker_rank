import sys

n = int(input())

list_n = [input().strip().split() for i in range(n)]
phone_book = {d[0].replace("'", ""): int(d[1]) for d in list_n}

lines = sys.stdin.readlines()
for line in lines:
    try:
        print(line.strip() + '=' + str(phone_book[line.strip()]))
    except:
        print('Not found')
