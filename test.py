# /usr/bin/python
# -*- encoding:utf-8 -*-

import sys
sys.stderr=open('log.txt','w+')
#sys.stdout=open(tt/'log.txt','w+')
raise Exception, 'this error will be logged' 
#print "this is a test"
#sys.stdout.close()
#sys.stderr.close()