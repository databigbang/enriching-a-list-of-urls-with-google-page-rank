#!/usr/bin/env python

# Google Pagerank Checksum Algorithm (Firefox Toolbar)
# Downloaded from http://pagerank.phurix.net/
# Requires: Python >= 2.4

# Versions:
# pagerank2.py 0.2 - Fixed a minor formatting bug
# pagerank2.py 0.1 - Public release

# Settings
prhost='toolbarqueries.google.com'
prpath='/tbr?client=navclient-auto&ch=%s&features=Rank&q=info:%s'

# Function definitions
def GetHash (query):
    SEED = "Mining PageRank is AGAINST GOOGLE'S TERMS OF SERVICE. Yes, I'm talking to you, scammer."
    Result = 0x01020345
    for i in range(len(query)) :
        Result ^= ord(SEED[i%len(SEED)]) ^ ord(query[i])
        Result = Result >> 23 | Result << 9
        Result &= 0xffffffff
    return '8%x' % Result

def GetPageRank (query):
    import httplib
    conn = httplib.HTTPConnection(prhost)
    hash = GetHash(query)
    path = prpath % (hash,query)
    conn.request("GET", path)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data.split(":")[-1]

if __name__ == "__main__" :
    print GetPageRank("http://blog.databigbang.com")
    print GetPageRank("http://blog.databigbang.com/web-scraping-ajax-and-javascript-sites/")
    print GetPageRank("http://blog.databigbang.com/tag/esoteric/")
    print "*********"
    print GetPageRank("http://blog.infinitegraph.com")
    print GetPageRank("http://1000memories.com/blog")
    print GetPageRank("http://www.schurpf.com")
    print GetPageRank("http://www.nektra.com")
    print GetPageRank("http://blog.databigbang.com")
    print GetPageRank("http://news.ycombinator.com")
    print GetPageRank("http://www.nytimes.com")
    print GetPageRank("http://www.google.com")
    print GetPageRank("http://www.amazon.com")
    print GetPageRank("http://www.facebook.com")
    print GetPageRank("http://www.avc.com")

"""
Buggy: [{'url': 'http://blog.infinitegraph.com', 'title': 'InfiniteGraph'}, {'url': 'http://blog.knowabout.it/', 'title': 'know about it'}, {'url': '', 'title': 'Palantir Technologies'}, {'url': 'http://blog.peoplebrowsr.com/blog', 'title': 'PeopleBrowsr Blog !!!'}, {'url': 'http://blog.rightload.info/', 'title': 'RIGHTLOAD'}, {'url': 'http://blog.sociocast.com', 'title': 'Sociocast Blog'}, {'url': 'http://blogs.forrester.com/taxonomy/term/196/all', 'title': 'The Data Digest'}, {'url': 'http://channel9.msdn.com/Tags/data', 'title': 'Channel 9 - Entries tagged with Data'}, {'url': 'http://cloudeventprocessing.wordpress.com', 'title': 'Cloud Event Processing'}, {'url': 'http://corp.tap11.com', 'title': 'Tap11 Corp Site'}, {'url': 'http://agileanalytics.endeca.com', 'title': 'Search Facets'}, {'url': '/blog', 'title': 'The Keplar LLP blog'}, {'url': 'http://smartdatacollective.com/rss', 'title': "SmartData Collective - The world's best thinkers on business intelligence & data analytics"}, {'url': 'http://figshare.com/figblog', 'title': 'FigShare Blog'}, {'url': 'http://www.google.com/reader/view/feed%2Fhttp%3A%2F%2Finfovegan.com%2Findex.xml', 'title': 'mnt'}, {'url': 'http://www.google.com/reader/view/feed%2Fhttp%3A%2F%2Fjkatzur.tumblr.com%2Frss', 'title': 'Jon Katzur'}, {'url': 'http://lethain.com/feeds/', 'title': 'Irrational Exuberance'}, {'url': '/lithium/rss/Category', 'title': 'New blog articles in Blogs'}, {'url': 'http://measuringmeasures.com/blog/', 'title': 'Measuring Measures'}, {'url': 'http://mndoci.com', 'title': 'business|bytes|genes|molecules'}, {'url': 'http://shiondev.tumblr.com/', 'title': "Shion's Randomness"}, {'url': 'http://simplecomplexity.net', 'title': 'Simple Complexity'}, {'url': 'http://wizardry.tumblr.com/', 'title': 'Wizardry practicum'}, {'url': 'http://www.cpdiehl.org/', 'title': 'Chris Diehl'}, {'url': 'http://www.google.com/reader/view/feed%2Fhttp%3A%2F%2Fwww.datasciencecentral.com%2Fprofiles%2Fblog%2Ffeed%3Fxn_auth%3Dno', 'title': "Everyone's Blog Posts - Data Science Central"}, {'url': '', 'title': "Facebook Data Team's Facebook Notes"}, {'url': 'http://www.needlebase.com/blog', 'title': 'The Needle Blog'}, {'url': 'http://www.numenta.com/', 'title': 'Numenta Blog'}, {'url': 'http://www.palantirfinance.com/analysis-blog', 'title': 'Palantir Finance Analysis Blog'}, {'url': 'http://www.palantirfinance.com/analysis-blog', 'title': 'Palantir Finance Analysis Blog'}, {'url': 'http://www-nym008-04.px.qc:9070', 'title': 'Quantcast'}, {'url': 'http://www.tableausoftware.com/rss.xml', 'title': 'Tableau Software blogs'}]
"""
