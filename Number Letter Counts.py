def numToWord(n):
  from math import log10, floor

  lenghtOf_n = floor(log10(n)+1)

  def split(n):
    if len(str(n)) > 2:
      if str(n) != '1':
        return f'{str(n)[0]}*{10**(len(str(n))-1)}'
      else:
        return f'{10**(len(str(n))-1)}'
    return str(n)
  
  def decompose(n):
    if lenghtOf_n >= 2:
      if str(n)[-2] != '1':
        digits = [split(int(str(n)[d])*10**(lenghtOf_n - d - 1)).split('*') for d in range(lenghtOf_n)]
        return digits
      else:
        digits = [split(int(str(n)[d])*10**(lenghtOf_n - d - 1)).split('*') for d in range(lenghtOf_n-2)]+[[str(n)[-2::]]]
    
        return digits

    else:
      return [[str(n)]]


  ones = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
  tens = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
  hunderds = {100:'hundred', 1000:'thousand'}

  onesLength = {a:len(b) for a,b in ones.items()}
  tensLength = {a:len(b) for a,b in tens.items()}
  hunderdsLength = {a:len(b) for a,b in hunderds.items()}

  decomposedN = [list(map(int, d)) for d in decompose(n)]

  s = 0
  w = ''
  for d in decomposedN:
    for d1 in d:
      try:
        s+=onesLength[d1]
        w+=ones[d1]
      except:pass
      try:
        s+=tensLength[d1]
        w+=tens[d1]
      except:pass
      try:
        s+=hunderdsLength[d1]
        w+=hunderds[d1]
      except:pass


  if n%100 != 0 and len(str(n))>2:
    return n,s+3,w,decomposedN



  return n,s,w,decomposedN


nums = [numToWord(n) for n in range(1, 1001)]
print(sum(sum(n[1] for n in nums)))
