from urllib import request, parse, error
from bs4 import BeautifulSoup as bs
import random
import datetime
import re
import sys


def request_page(url_req):
	rsp=request.urlopen(url_req)
	if rsp.status==200:
		return rsp
	else:
		print("problem requesting the page occured!")
		return "response code:"+str(rsp.status)


def get_urls(rel_url):
	"""gets urls from wiki article"""
	#wiki main page url
	main='https://en.wikipedia.org/'
	#article url
	url=parse.urljoin(main,rel_url)
	#header info
	req_head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	#construct the reqauest header
	req=request.Request(url, headers=req_head)
	#request the page
	rsp=request_page(req)
	
	new_urls=[]
	link_patt=re.compile('^(/wiki/)((?!:).)*$')
	
	#parse the html
	soup=bs(rsp.read(),'lxml')
	
	body=soup.find('div',attrs={'id':'bodyContent'})
	#check if body is None
	if body is None:
		print("error occured! body is None!")
		return None
	#look for anchor tags <a> with matching href attributes
	for link in body.find_all('a',attrs={'href':link_patt}):
		new_urls.append(link.get('href'))
	
	return new_urls


def random_walk(start):
	"""randomly walks through wiki articles"""
	global start_url
	global pages
	#set the random seed
	now=datetime.datetime.now()
	random.seed(now)
	
	#request the page and get the links
	print('started from: {}\n now at: {}\n count: {}'.format(start_url, start, pages))
	print("-"*50)
	link_list=get_urls(start)
	
	#randomly choose a link
	while len(link_list)>0:
		new_url=random.choice(link_list)
		if new_url == start_url:
			break
		else:
			pages+=1
			random_walk(new_url)
			
	
	return pages


def get_internal_links(start):
	"""returns a list of internal urls"""
	global internal_links
	
	#request the page
	page=request_page(start)
	
	#parse page html
	soup=bs(page.read(),'lxml')
	
	#extract domain name
	domain=start.split('.')[-2]
	
	#pattern for internal links
	patt=re.compile('^(/|.*'+domain+')')
	
	#list to save found urls
	internals=set()
	
	#add current page
	internals.add(start)
	
	#find all links in the page
	for link in soup.find_all('a',attrs={'href':patt}):
		url=link.get('href')
		#complete relative urls
		url=parse.urljoin(start,url)
		
		if not url in internal_links:
			internals.add(url)
	
	return internals


def get_external_links(start):
	"""returns all external links from a page"""
	global external_lins
	global internal_links
	
	#variavle to save the found links
	externals=set()
	
	#request the page
	page=request_page(start)
	#parse the page html
	html=bs(page.read(),'lxml')
	
	#look for all links that fit the external lonk pattern
	#get domain name
	domain=start.split('.')[-2]
	
	#pattern
	patt=re.compile('^(www|http)((?!{}).)*$'.format(domain))	
	
	#get all anchor tags fitting the pattern
	for link in html.find_all('a',attrs={'href':patt}):
		url=link.get('href')
		
		if not url in external_links:
			externals.add(url)
	
	return externals


def site_dig(start):
	"""digs through the site for internal and external links"""
	global internal_links
	global external_links
	global visited
	
	#skip if visited before
	if start in visited:
		print('visited before')
		return None
	
	else:
		visited.append(start)
		print(start)
	
	#internal links dig
	internals=get_internal_links(start)
	externals=get_external_links(start)
	
	#update globals
	internal_links.update(internals)
	external_links.update(externals)
	
	#recurse
	for url in internals:
		try:
			site_dig(url)
		except:
			print("can't access",url)
			print()
			continue
		print('digging',url)
		print()
	
	



#starting page url
start_url='https://www.oreilly.com/'
internal_links=set()
#internal_links.update(get_internal_links(start_url))
external_links=set()
#external_links.update(get_external_links(start_url))
visited=[]
#pages=1
site_dig(start_url)
#print(random_walk(start_url))
print('\n'.join(external_links))

