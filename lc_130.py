from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        if m < 3:
            return
        
        visited = [[False]*n for i in range(m)]
        currrentArea = []
        flag = False

        def walk(i,j):
            nonlocal flag, currrentArea, visited, board
            if  i == 0 or j == 0 or i == m-1 or j == n-1:
                flag = False
            visited[i][j] = True
            currrentArea.append([i,j])
            if j+1 < n and not visited[i][j+1] and board[i][j+1] == 'O':
                visited[i][j+1] = True
                walk(i, j+1)
            if i+1 < m and not visited[i+1][j] and board[i+1][j] == 'O':
                visited[i+1][j] = True
                walk(i+1, j)
            if i-1 >= 0 and not visited[i-1][j] and board[i-1][j] == 'O':
                visited[i-1][j] = True
                walk(i-1, j)
            if j-1 >= 0 and not visited[i][j-1] and board[i][j-1] == 'O':
                visited[i][j-1] = True
                walk(i, j-1)

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and board[i][j] == 'O':
                    flag = True
                    walk(i,j)
                    print(currrentArea, flag)
                    if flag:
                        for point in currrentArea:
                            board[point[0]][point[1]] = 'X'
                    currrentArea = []
                    flag = True


if __name__ == '__main__':
   s = Solution()
   sample = [["O","X","O","O","X","X"],["O","X","X","X","O","X"],["X","O","O","X","O","O"],["X","O","X","X","X","X"],["O","O","X","O","X","X"],["X","X","O","O","O","O"]]
   s.solve(sample)
   print(sample)