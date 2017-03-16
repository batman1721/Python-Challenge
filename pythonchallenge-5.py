#Python Challenge 5

import urllib2, pickle
 
url = 'http://www.pythonchallenge.com/pc/def/banner.p'
code = pickle.loads(urllib2.urlopen(url).read())
print code
for line in code:
    print ''.join(elmt[0] * elmt[1] for elmt in line)
