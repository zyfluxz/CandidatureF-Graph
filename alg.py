
Edges = [(0,1),(1,2),(2,3),(3,4),(4,0),
     (0,5),(1,6),(2,7),(3,8),(4,9),
     (5,7),(7,9),(9,6),(6,8),(8,5)]

Vertices = {"A":[0,5],"B":[1,6],"C":[2,7],"D":[3,8],"E":[4,9]}

def getAl(i):
  for k in Vertices:
    if i in Vertices[k]: return k
  return None

class Node():
  
  def __init__(self, n):
    self.n = n
    self.ngb = []
    
nodes = [Node(i) for i in range(10)]

for e in Edges:
  a, b = e
  nodes[a].ngb += [b]
  nodes[b].ngb += [a]

def ngbAl(i,al):
  ret = []
  for g in nodes[i].ngb:
    if getAl(g) == al:
      ret += [g]
  return ret

#print ngbAl(0,"A")

T = 10
for t in range(T):
  K = raw_input()
  mi = None
  for p in Vertices[K[0]]:
    G = K[1:]
    T = [p]
    f = 1
    while G:
      l = ngbAl(p, G[0])
      if len(l) == 0:
        f = 0
        break
      assert len(l) == 1
      p = l[0]
      G = G[1:]
      T += [p]
    if f:  
      st = "".join(map(str,T))
      if mi == None:
        mi = st
      elif mi > st:
        mi = st
  if mi is None: print -1
  else: print mi            
            
