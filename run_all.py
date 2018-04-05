import os 
import searchengine

fn = 'searchindex.db'
if( False ): os.unlink(fn) # execute if we want to "recrawl" the Perl web pages 

crawler = searchengine.crawler(fn)
crawler.createindextables()

# crawl some pages: 
#pagelist=['https://en.wikipedia.org/wiki/R_(programming_language)']
#crawler.crawl(pagelist)

pagelist = ['http://www.diveintopython.net']
crawler.crawl(pagelist)

[row for row in crawler.con.execute('select rowid from wordlocation where wordid=1')] 

import neuralnetwork as nn
mynet = nn.searchnet('nn.db')
mynet.maketables()

wordstosearch = 'python'
e = searchengine.searcher('searchindex.db')
e.getmatchrows(wordstosearch)

# create the needed tables for the page rank algorithm:
crawler.calculatepagerank()

# before adding in the page rank algorithm into the weights that form the scoring function 
e.query(wordstosearch) 

cur = crawler.con.execute('select * from pagerank order by score desc')
#for i in range(3): print(cur.next())
e.geturlname(17)  # word "python" rowid==17

# after adding in the page rank algorithm into the weights that form the scoring function
import importlib
importlib.reload(searchengine)
e = searchengine.searcher('searchindex.db')
e.query(wordstosearch) 

# after adding in the linktextscore algorithm into the weights that form the scoring function 

importlib.reload(searchengine)
e = searchengine.searcher('searchindex.db')
e.query(wordstosearch) 


# starting the neural network click learning:
#
# import neuralnetwork as nn
# mynet = nn.searchnet('nn.db')
# mynet.maketables()

wWorld,wRiver,wBank = 101,102,103
uWorldBank,uRiver,uEarth = 201,202,203
mynet.generatehiddennode( [wWorld,wBank], [uWorldBank,uRiver,uEarth])

for c in mynet.con.execute('select * from hiddenurl' ): print(c)

mynet.getresult([wWorld,wBank],[uWorldBank,uRiver,uEarth])
mynet.trainquery([wWorld,wBank],[uWorldBank,uRiver,uEarth],uWorldBank)
mynet.getresult([wWorld,wBank],[uWorldBank,uRiver,uEarth])

allurls = [ uWorldBank, uRiver, uEarth ]
for i in range(30):
    mynet.trainquery([wWorld,wBank],allurls,uWorldBank)
    mynet.trainquery([wRiver,wBank],allurls,uRiver)
    mynet.trainquery([wWorld],allurls,uEarth)

mynet.getresult([wWorld,wBank],allurls)
mynet.getresult([wRiver,wBank],allurls)
mynet.getresult([wBank],allurls)





