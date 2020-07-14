T = int(input())
for i in range(0,T):
    odd_n = []
    even_n = []
    for count,ele in enumerate(input()):
        if count % 2 == 0:
            even_n.append(ele)
        else:
            odd_n.append(ele)
    print(''.join(even_n),''.join(odd_n))