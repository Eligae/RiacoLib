from itertools import combinations, permutations
__doc__="""
more short words to use in math
"""


def factorial(n:int)->int:
    """
    n! 을 연산        
    """
    temp = 1
    while n > 0:
        temp *= n
        n -= 1
    return temp

def nCr(n:int, r:int)->list:
    """
    nCr 경우를 list로 출력
    """
    elements = [i for i in range(1, n+1)]
    return list(combinations(elements, r))

def nPr(n:int, r:int)->list:
    """
    nPr 경우를 list로 출력
    """
    elements = [i for i in range(1, n+1)]
    return list(permutations(elements, r))