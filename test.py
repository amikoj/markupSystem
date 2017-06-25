# /usr/bin/python
# -*- encoding:utf-8 -*-

import sys,codecs
#sys.stderr=open('log.txt','w+')
#sys.stdout=open(tt/'log.txt','w+')
#raise Exception, 'this error will be logged' 
#print "this is a test"
#sys.stdout.close()
#sys.stderr.close()

#with codecs.open('test_text.txt',mode='r',encoding='utf-8') as input_file:
    #print input_file.read()
source_file = 'test_text.txt'
target_file="%s.html" % source_file[:str(source_file).rindex('.')]
print target_file