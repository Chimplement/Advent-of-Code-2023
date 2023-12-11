u=open(0).read().split("\n")
e=lambda x,y:sum(999999*(n<x)for n in y)
P=sum([[(e(x,[i for i in range(len(u[0]))if all(False for l in u if l[i]=="#")])+x,e(y,[i for i,l in enumerate(u)if l.count("#")==0])+y)for x,h in enumerate(l)if h=="#"]for y,l in enumerate(u)],[])
print(sum(sum([[abs(q[0]-p[0])+abs(q[1]-p[1])for q in P]for p in P],[]))//2)