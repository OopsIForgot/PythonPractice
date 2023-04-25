"""
이름 : 황재찬
학번 : 2020039040
"""

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if a[j-1] > a[j]:
                a[j-1],a[j] = a[j],a[j-1]

if __name__ == '__main__':
    print('버블 정렬을 수행합니다.')
    n = int(input("원소 수를 입력하세요. : "))
    x = [0]*n

    for i in range(n):
        x[i] = int(input(f'x[{i}]:'))
    
    bubble_sort(x)

    print('오름차순으로 정렬했습니다. ')
    for i in range(n):
        print(f'x[{i}] = {x[i]}')
        
