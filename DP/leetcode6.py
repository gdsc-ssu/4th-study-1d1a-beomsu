"""
14
3*7

10    12
20 21 22
30    32

중간 여부 확인을 어떻게 할지?
대각선으로 올라가는 행동과 일직선으로 내려가는 행동을 구별하는 플래그를 두자.
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag: Array[Array[str]] = [[] for i in range(numRows)]
        print(zigzag)

        isZig: bool = False

        row: int = -1

        for i in s:
            match isZig:
                case False:
                    if row < numRows - 1:
                        row += 1
                    elif row == numRows - 1:
                        isZig = True
                        row -= 1
                    
                    zigzag[row].append(i)
                case True:
                    if row > 0:
                        row -= 1
                    elif row == 0:
                        isZig = False
                        row += 1
                        
                    zigzag[row].append(i)
                        
        answer: str = ""
        for i in zigzag:
            for j in i:
                answer += j
        
        return answer