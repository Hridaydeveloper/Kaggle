def is_safe(queens, row, col):
  for r in range(row):
    c = queens[r]
    if c == col or abs(r - row) == abs(c - col):
      return False
  return True

def solve(queens, row, n):
  if row == n:
    return True

  for col in range(n):
    if is_safe(queens, row, col):
      queens.append(col)
      if solve(queens, row + 1, n):
        return True
      queens.pop()
  return False

n = 5
queens = []
if solve(queens, 0, n):
  for col in queens:
    print(["Q" if c == col else "." for c in range(n)])
