#!/usr/bin/python

# Used for sending blog bundles retrieved from Google Reader.
# Page Rank sorting from http://www.schurpf.com/google-pagerank-python/ and https://github.com/phurix/pagerank


import time
import sys
from lxml import etree
from lxml.html import builder as E
import lxml.html
import pagerank
import argparse


def main():
	parser = argparse.ArgumentParser(description='Get an HTML table from an OPML file with web resources ordered by Google PageRank.')
	parser.add_argument('--input', nargs=1, required=True, help='name of the OPML input file')
	parser.add_argument('--output', nargs=1, required=True, help='name of the HTML output file')
	args = parser.parse_args()

	input_file = args.input[0]
	output_file = args.output[0]

	tree = etree.parse(input_file)
	elems = tree.xpath("//opml/body/outline/outline")
	counter = 0
	buggy = []
	urls = []
	for elem in elems:
		url = elem.attrib["htmlUrl"]
		title = elem.attrib["title"]
		pr = False
		retries = 3
		while retries != 0:
			try:
				pr = int(pagerank.GetPageRank(url))
				retries = 0
			except Exception as e:
				retries -= 1
				time.sleep(3)

		if pr != False:
			print url, title, pr
			urls.append({'title':title, "url":url, "pagerank":pr})
			counter += 1
		else:
			buggy.append({'url':url, 'title':title})

	f = open(output_file, "w")
	headers = ["Title", "URL", "PageRank"]
	sorted_urls = sorted(urls, key=lambda k:k["pagerank"])
	sorted_urls_as_a_list = []
	sorted_urls.reverse()

	style = "border: 1px solid black"
	for elem in sorted_urls:
		print elem["title"], elem["url"], elem["pagerank"]
		sorted_urls_as_a_list.append(E.TR(E.TD(elem["title"], style=style), E.TD(E.A(elem["url"],href=elem["url"]), style=style), E.TD(str(elem["pagerank"]), style=style)))
	html = E.HTML(E.HEAD(), E.BODY(E.TABLE(*tuple(sorted_urls_as_a_list), style="border: 1px solid black; border-collapse: collapse")))

	htmlcode = lxml.html.tostring(html)

	f.write(htmlcode)
	f.close()



if __name__ == '__main__':
	main()
