import random

def bin(n, p):
  x = 0.0
  for i in range(n):
    if random.random() <= p:
      x += 1
  return x

def geo(p) :
  x = 0
  while random.random() > p :
    x += 1
  return x

def avggeo(p):
  total = 0
  for i in range(100000):
    total += geo(p)
  return total/100000.0

def hypgeo(k, p) :
  x = 0
  succ = 0
  while succ < 5 :
    while random.random() > p :
      x += 1
    succ += 1
  return x

def poi(n, l) :
  return bin(n, l/float(n))

def exp(n, l):
  return geo(l/float(n))

def avgexp(n,l):
  total = 0
  for i in range(1000):
    total += geo(l/float(n))
  return total/1000.0

print 'bin ', bin(20, 0.4)
print 'geo ', geo(0.03)
print 'avggeo ', avggeo(0.03)
print 'hypgeo ', hypgeo(5, 0.03)
print 'poi ', poi(60000, 3.1)
print 'exp', exp(60000, 3.1)