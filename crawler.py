import urllib 

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
		if url : 
			return all_links
		else : 
			all_links.append(url)
			page = page[index + 1 :]	



page = get_page('http://xkcd.com/353') 
links = get_all_links(page)

for l in links : 
	print l