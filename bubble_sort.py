from random import randint

def bubble(l):
	sort=time=0
	while not sort:
		sort=1
		for ind in xrange(1,len(l)):
			if l[ind-1]>l[ind]:
				l[ind-1],l[ind]=l[ind],l[ind-1]
				sort*=0
		time+=1
	return l,len(l),time,time*len(l)

l=[randint(1,100) for i in xrange(1000)]

#print l
print
print bubble(l)

