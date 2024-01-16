#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Самостоятельно изучите работу со стандартным пакетом Python timeit.
# Оцените с помощью этого модуля скорость работы итеративной
# и рекурсивной версий функций factorial и fib . Во сколько раз изменится
# скорость работы рекурсивных версий функций factorial и fib
# при использовании декоратора lru_cache? Приведите в отчет и
# обоснуйте полученные результаты.


import timeit
from functools import lru_cache


# Итеративная версия функции factorial
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


# Рекурсивная версия функции factorial
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)


# Итеративная версия функции fibonacci
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# Рекурсивная версия функции fibonacci
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


# Рекурсивная версия функции factorial с использованием lru_cache
@lru_cache
def factorial_recursive_lru(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive_lru(n-1)


# Рекурсивная версия функции fibonacci с использованием lru_cache
@lru_cache
def fib_recursive_lru(n):
    if n <= 1:
        return n
    else:
        return fib_recursive_lru(n-1) + fib_recursive_lru(n-2)


if __name__ == '__main__':
    # Оценка скорости работы итеративной и рекурсивной версий функций
    print("Factorial итеративный:", timeit.timeit(lambda: factorial_iterative(10), number=100000))
    print("Factorial рекурсивный:", timeit.timeit(lambda: factorial_recursive(10), number=100000))
    print("Fibonacci итеративный:", timeit.timeit(lambda: fib_iterative(10), number=100000))
    print("Fibonacci рекурсивный:", timeit.timeit(lambda: fib_recursive(10), number=100000))

    # Оценка скорости работы рекурсивных версий функций с использованием lru_cache
    print("Factorial рекурсивный с @lru_cache:", timeit.timeit(lambda: factorial_recursive_lru(10), number=100000))
    print("Fibonacci рекурсивный с @lru_cache:", timeit.timeit(lambda: fib_recursive_lru(10), number=100000))
