def fact(n):
  if n in [0, 1]:
    return n
  return n * fact(n-1)

def nCr(n, r):
  return fact(n) // (fact(n-r) * fact(r))

print(nCr(5, 2))