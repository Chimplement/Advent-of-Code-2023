import math
def z(n,s=0):
	while n[2]!='Z':n=m[n][d[s%len(d)]];s+=1
	return s
i=open(0).readlines()
d=[c!='L'for c in i[0][:-1]]
m={l[:3]:(l[7:10],l[12:15])for l in i[2:]}
print(math.lcm(*[z(n)for n in m if n[2]=='A']))