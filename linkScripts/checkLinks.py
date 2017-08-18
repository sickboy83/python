import sys
from urlparse import urlparse
from BeautifulSoup import BeautifulSoup
import urllib2
import re
import requests

def getLinks(url, result, base):
    try:
        # get page
        html_page = urllib2.urlopen(url)
        print url
    except urllib2.HTTPError:
        print 'Error on ',url
        return result
    except urllib2.URLError:
        print 'Error on ',url
        return result
    except ValueError:
        print 'Error on ',url
        return result
    except AttributeError:
        print 'Error on ',url
        return result

    soup = BeautifulSoup(html_page)
    links = soup.findAll('a')
    # foreach link in page
    for link in links:
        if '#' in link.get('href'):
            print "Found '#' on ", url
        if base in link.get('href') and link.get('href') not in result and link.get('href') != None:
            result.append(link.get('href'))
            result.extend(getLinks(link.get('href'), result, base))

    return result

# Expecting URL as parameter
if len(sys.argv) != 2:
    print 'File path needed'
    sys.exit(0)

url = sys.argv[1]
base = urlparse(url).netloc
baseArray = base.split('.')
if 3 == len(baseArray):
    base = ''.join((baseArray[1], '.', baseArray[2]))

pages = []
getLinks(url, pages, base)
