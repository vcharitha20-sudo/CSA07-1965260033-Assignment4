"""Check whether critical sites E and F survive every single link failure."""
from itertools import combinations
SITES = 'ABCDEF'
LAKH_PER_LINK = 1.2 + 2*0.25
TOPOLOGIES = {
 'bus': [('A','B'),('B','C'),('C','D'),('D','E'),('E','F')],
 'ring': [('A','B'),('B','C'),('C','D'),('D','E'),('E','F'),('F','A')],
 'star': [(s,'D') for s in 'ABCEF'],
 'mesh': list(combinations(SITES,2)),
 'hybrid': [('D','E'),('E','F'),('F','D'),('A','D'),('B','D'),('C','D')]
}
def reachable(edges,start):
 seen={start}; stack=[start]
 while stack:
  node=stack.pop()
  for a,b in edges:
   nxt=b if a==node else a if b==node else None
   if nxt and nxt not in seen:seen.add(nxt);stack.append(nxt)
 return seen
for kind,edges in TOPOLOGIES.items():
 ok=sum({'E','F'} <= reachable([e for e in edges if e!=broken],'D') for broken in edges)
 print(f'{kind:<6} links {len(edges):2d} cost Rs {len(edges)*LAKH_PER_LINK:5.1f} lakh E and F survive {ok}/{len(edges)} cuts')
