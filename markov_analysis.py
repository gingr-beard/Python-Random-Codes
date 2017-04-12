'''
analyze a text for words relations
#open the text file
#read lines, remove punctuations, lower the case
#test:
half a bee philosophically must ipso facto half not be but half the bee has got to be vis a vis its entity d’you see but can a bee be said to be or not to be an entire bee when half the bee is not a bee due to some ancient injury
'''


def file_process(file_name):
	
	opener=open(filename,'r')
	
	file_mark={}
	
	for line in opener:
		line_mark=line_process(line)
	
	file_mark=dict_combine(file_mark,line_mark)
	
	return file_mark


def line_process(line):
	import string
	from txt_trans import trans
	
	markov={}
	
	#making translate table to remove punctuation marks
	line=trans(trans(line,string.whitespace,' '),string.punctuation,'').lower()
	
	parse=markov_analysis(line)
	
	markov=dict_combine(markov,parse)
	
	return markov
	
	
def markov_analysis(txt):
	#apply markov analysis to a text
	import re
	
	tmp=txt.split()
	markov={k:None for k in tmp}
	
	patt='{} (\w*)'
	
	for word in tmp:
		markov[word]=re.findall(patt.format(word),txt)
	
	return markov
	

def dict_combine(d1,d2):
	#d1[k]+=d2[k]
	for k in d2.keys():
		d1[k]=d1.get(k,d2[k]*0)+d2[k]
	
	return d1

line='half a bee philosophically must ipso facto half not be but half the bee has got to be vis a vis its entity d’you see but can a bee be said to be or not to be an entire bee when half the bee is not a bee due to some ancient injury'
print(line_process(line))
