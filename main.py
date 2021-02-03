def primeDecomposition(N) : 
  i, primes = 2, set([]) 
  while i*i <= N :
    # If N is divisible by i then i is a factor of N
    if N%i == 0 : 
      N = N / i
      primes.add(i)
    # If N is not divisible by i then i is not a factor 
    # of N and we should try the next highest number
    else : 
      i = i + 1 
  if N>1 : primes.add(N)
  return primes 
  
for i in range(2,20) : 
  print("The largest prime factor of", i, "is", primeDecomposition(i) )
