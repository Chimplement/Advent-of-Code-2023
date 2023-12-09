n=lambda s:s[-1]+n([s[j]-s[j-1]for j in range(1,len(s))])if any(s)else 0
print(sum(n([int(w)for w in l.split()][::-1])for l in open(0).readlines()))