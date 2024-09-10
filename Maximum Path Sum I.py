triangle = """

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
ntriangle = [list(map(int, triangle.split('\n')[i].split())) for i in range(len(triangle.split('\n'))) if triangle.split('\n')[i] != '']
ntriangle
#51+95=146
#51+66=117
#
def neighbors(n:tuple) -> list:
  a, b = n
  if b+1<len(ntriangle) :
    if a+1 < len(ntriangle[b+1]):
      return {ntriangle[b+1][a]:(a,b+1), ntriangle[b+1][a+1]:(a+1,b+1)}
    else:
      return [0,0]
  return [0,0]


def sumNeighborsToSelf(n:tuple):
  i, j = n
  N =  neighbors(n)
  number = ntriangle[j][i]
  return {number + neighbor:[number, n] for neighbor in N}

i = 0
start = (0,0)
path = [[ntriangle[0][0], start]]
while start[1] < len(ntriangle)-1:
  N = neighbors(start)
  SN = [sumNeighborsToSelf(N[neighbor]) for neighbor in N]
  SN1 = {}

  for d in SN:
      SN1.update(d)
  SN = SN1

  nextstart = SN[max(SN)][1]
  path.append(SN[max(SN)])
  start = nextstart

  i +=1

path
npath = sum([n[0] for n in path])
npath
