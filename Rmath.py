from itertools import combinations

class Rmath():
    def factorial(self, n:int)->int:
        """
        n! 을 연산
        """
        temp = 1
        while n > 0:
            temp *= n
            n -= 1
        return temp
    def nCr(self, n:int, r:int)->list:
        """
        nCr 경우를 list로 출력

        예시 : [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
        """
        elements = [i for i in range(1, n+1)]
        return list(combinations(elements, r))
