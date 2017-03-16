#Python Challenge 4

import urllib2

code=12345
for i in xrange(0,400):
    myurl='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(code)
    response=urllib2.urlopen(myurl)
    code=response.read().split(' ')[5]

print myurl
