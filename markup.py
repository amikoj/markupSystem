# /usr/bin/python
# -*-encoding:utf-8 -*-

import sys,re,time,os
from markup.util import *
from markup.handlers import  *
from markup.rules import *
from markup.parse import *


#log file set


formate_times=time.strftime(format('%Y-%m-%d'))
LOG_FILE_DIR='logs'
LOG_ERROR_FILE='error_%s.txt' % formate_times
LOG_OUT_FILE='log_%s.txt'% formate_times
temp=sys.stdout
def start_log():
    if os.path.exists(LOG_FILE_DIR):
        os.mkdir(LOG_FILE_DIR)
    sys.stdout=open(LOG_FILE_DIR+"/"+LOG_OUT_FILE,'w')
    sys.stderr=open(OG_FILE_DIR+"/"+LOG_ERROR_FILE,'w')



def stop_log():
    sys.stdout.close()
    sys.stderr.close()
    sys.stdout=temp
    
    
def usage():
    stop_log()
    print "Markup tool"
    print ""
    
    
    start_log()
    
    
def main():
    print "begin handler this week."



start_log()
if __name__ == '__main__':
    print "this is main program."















        
handler=HTMLRenderer()
parse = BasicTextParser(handler)
parse.parse(sys.stdin)