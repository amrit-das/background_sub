import sys
c=0
def add(n):
	global c
	n+=1
	print n
	c*=(1000**n)
	sys.setrecursionlimit(1500)
	add(n)
add(1)