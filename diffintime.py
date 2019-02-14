h1,m1=map(int,input().split())
h2,m2=map(int,input().split())
if h1>h2:
	h=h1-h2
else:
	h=h2-h1
	
if m1>m2:
	m=m1-m2
else:
	m=m2-m1
print(h,m)
