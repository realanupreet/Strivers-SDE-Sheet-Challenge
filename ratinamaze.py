from typing import List

def ratMaze(matrix: List[List[int]]) -> List[str]:
  n = len(matrix)
  paths = []

  def _dfs(i, j, path):
    if i == n - 1 and j == n - 1:
      paths.append(path)
      return

    if matrix[i][j] == 0:
      return

    path.append("D")
    if i < n - 1:
      _dfs(i + 1, j, path)

    path.append("R")
    if j < n - 1:
      _dfs(i, j + 1, path)

    path.pop()
    path.pop()

  _dfs(0, 0, [])
  return paths