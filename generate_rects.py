import random

N = 1024

print(N)
for _ in range(N):
  x = random.randint(-100, 100)
  y = random.randint(-100, 100)
  w = random.randint(2, 15)
  h = random.randint(2, 15)

  print(x, y, x+w, y+h)
