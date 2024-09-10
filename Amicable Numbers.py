def properDivs(n):
  return [d for d in range(1,n) if n%d==0]
def sumProperDivs(n):
  return sum(properDivs(n))
def areAmicable(a, b):
  if (a != b) and (sumProperDivs(a) == b)  and (sumProperDivs(b) == a):return True
  return False
areAmicable(220, 284)
Anumbers = []
a = 2
while a < 10**4:
  b = sumProperDivs(a)
  if sumProperDivs(b) == a and b!=a:
    Anumbers.append(a)
  a+=1

Anumbers
sum(Anumbers)
