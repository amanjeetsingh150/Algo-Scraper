import urllib2
from bs4 import BeautifulSoup

def algoinfo():
    urllist=['https://en.wikipedia.org/wiki/Bubble_sort',
         'https://en.wikipedia.org/wiki/Heapsort',
         'https://en.wikipedia.org/wiki/Quicksort',
         'https://en.wikipedia.org/wiki/Merge_sort',
         'https://en.wikipedia.org/wiki/Selection_sort',
         'https://en.wikipedia.org/wiki/Insertion_sort']
    for x in urllist:
        infofile=urllib2.urlopen(x)
        infohtm=infofile.read()
        infofile.close()
        soup=BeautifulSoup(infohtm,'html.parser')
        p=soup.find_all('p')
        if x=='https://en.wikipedia.org/wiki/Merge_sort':
            print p[1].text
        else:
            print p[0].text

def searchinginfo():
    urllist=['https://en.wikipedia.org/wiki/Binary_search_algorithm',
             'https://en.wikipedia.org/wiki/Linear_search']
    for i in urllist:
        searchfile=urllib2.urlopen(i)
        searchhtm=searchfile.read()
        searchfile.close()
        soup=BeautifulSoup(searchhtm,'html.parser')
        p=soup.find_all('p')
        print p[0].text
    

if __name__ == '__main__':
    algoinfo()
    searchinginfo()
        
