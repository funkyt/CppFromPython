def overlap1(i1, i2):
  return i2[0] < i1[1] and i2[1] < i1[0]

def overlap2(r1, r2):
  return overlap1(r1[:2], r2[:2]) and overlap1(r1[2:], r2[2:])

count = 0
rects = []
N = int(input())
for _ in range(N):
  rect = [int(x) for x in input().split()]
  assert len(rect) == 4
  for other in rects:
    count += 1 if overlap2(rect, other) else 0
  rects.append(rect)
print(count)