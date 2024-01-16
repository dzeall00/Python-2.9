#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Даны целые числа m и n, где 0 ≤ m ≤ n, вычислить, используя рекурсию, 
# число сочетаний С(n, m) , по формуле: С(0,n)=C(n,n)=1, C(m,n)=C(m,n-1)+C(m-1,n-1) при 0 ≤ m ≤ n. 
# Воспользовавшись формулой C(m,n)=n!/m!(n-m)! можно проверить правильность результата.


def C(m, n):
    if m == n or m == 0:
        return 1
    elif 0 <= m <= n:
        return C(m, n - 1) + C(m - 1, n - 1)

if __name__ == '__main__':
    print(C(int(input()), int(input())))
