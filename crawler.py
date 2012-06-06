import urllib 
import listHelper

def get_page(url) : 
	try : 
		return urllib.urlopen(url).read() 
	except: 
		return None 


def get_next_url(page) : 
	START_LINK = "<a href"
	QUOTE = '"'

	url_loc = page.find(START_LINK)

	if url_loc == -1 :
		return None, 0
	else : 
		start_quote = page.find(QUOTE, url_loc + 1)
		end_quote = page.find(QUOTE, start_quote + 1)
		url = page[start_quote + 1 : end_quote]

		return url, end_quote


def get_all_links(page) : 
	all_links = []

	while True : 
		url, index = get_next_url(page)
		if url is None : 
			return all_links
		else : 
			all_links.append(url)
			page = page[index + 1 :]	


def crawl(seed_url) : 
	seed_page = get_page(seed_url)
	to_crawl = get_all_links(seed_page)
	crawled = [] 
	index = []

	while to_crawl:

		# getting the first element from the list
		url_to_crawl = to_crawl.pop(0)

		# get page source and extract all the links
		crawled_page = get_page(url_to_crawl)
		links = get_all_links(crawled_page)

		add_page_to_index(index, url_to_crawl, crawled_page)

		# find all the links that are not already crawled and append new ones 
		# to be to_crawl list 
		un_crawled_links = listHelper.get_non_intersecting(links, crawled)
		listHelper.union(to_crawl, un_crawled_links)
		crawled.append(url_to_crawl)

	return index


def add_to_index(index, keyword, url) :
	for pairs in index : 
		if pairs[0] == keyword : 
			pairs[1].append(url)
			return	
	index.append([keyword, [url]])


def lookup(index,keyword):
	for pair in index:
	    if pair[0] == keyword : 
	        return pair[1]
	return []


def add_page_to_index(index,url,content):
	words = content.split() 
	for word in words: 
	    add_to_index(index, word, url)


if __name__ == "__main__" : 
	index = crawl('http://www.udacity.com/cs101x/index.html')
	listHelper.printList(index)