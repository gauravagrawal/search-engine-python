# This is a search engine code in python. It was developed as part of 
# Udacity course. 
# Copyright (C) 2012  Gaurav Agrawal
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


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
	index = {}
	graph = {}

	while to_crawl:

		# getting the first element from the list
		url_to_crawl = to_crawl.pop(0)

		# get page source and extract all the links
		crawled_page = get_page(url_to_crawl)
		links = get_all_links(crawled_page)

		add_page_to_index(index, url_to_crawl, crawled_page)
		add_to_graph(graph, url_to_crawl, links)

		# find all the links that are not already crawled and append new ones 
		# to be to_crawl list 
		un_crawled_links = listHelper.get_non_intersecting(links, crawled)
		listHelper.union(to_crawl, un_crawled_links)
		crawled.append(url_to_crawl)

	return index, graph


def compute_ranks(graph) : 
	damping_factor = 0.8 # probability whether they gonna follow link from current page or go to some other random link
	numLoops = 10

	ranks = {} 
	npages = len(graph)

	for page in graph : 
		ranks[page] = 1.0 / npages

	for i in range(0, numLoops) : 
		newranks = {} 
		for page in graph : 
			newrank = (1 - damping_factor) / npages
			for node in graph: 
				if page in graph[node] : 
					newrank = newrank + damping_factor * (ranks[node] / len(graph[node])

			newranks[page] = newrank
		ranks = newranks
	return ranks

def add_to_graph(graph, url, outlinks) : 
	if url not in graph : 
		graph[url] = outlinks 
	else :
		for link in outlinks : 
			if link not in graph[url] : 
				graph[url].append(link)

def add_to_index(index, keyword, url) :
	if keyword in index : 
		index[keyword].append(url)
	else : 
		index[keyword] = [url]


def lookup(index,keyword):
	if keyword in index : 
		return index[keyword]
	return None 


def add_page_to_index(index,url,content):
	words = content.split() 
	for word in words: 
	    add_to_index(index, word, url)


def lucky_search(index, ranks, keyword) : 
	pages = lookup(index, keyword)
	if not pages :
		return None 

	best_page = pages[0]
	for candidate in pages : 
		if candidate in ranks : 
			if ranks[candidate] > ranks[best_page] : 
				best_page = candidate
	return best_page


if __name__ == "__main__" : 
	index, graph = crawl('http://www.udacity.com/cs101x/index.html')
	print graph