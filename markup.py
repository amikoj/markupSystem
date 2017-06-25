# /usr/bin/python
# -*-encoding:utf-8 -*-

import sys,time,os,getopt,codecs
from markup.parser import *



#log file set
formate_times=time.strftime(format('%Y-%m-%d'))
LOG_FILE_DIR='logs'
LOG_ERROR_FILE='error_%s.txt' % formate_times
LOG_OUT_FILE='log_%s.txt'% formate_times
temp=sys.stdout

#global params
default_output_file = True
source_file = ""
target_file = ""


def start_log():
    '''
    log file 
    '''
    if not os.path.exists(LOG_FILE_DIR):
        os.mkdir(LOG_FILE_DIR)
    sys.stdout=open(LOG_FILE_DIR+"/"+LOG_OUT_FILE,'aw')
    sys.stderr=open(LOG_FILE_DIR+"/"+LOG_ERROR_FILE,'aw')



def stop_log():
    sys.stdout.close()
    sys.stderr.close()
    sys.stdout=temp
    
    
def usage():
    #stop_log()
    print "Markup tool"
    print  ""
    print "Usage:  python markup .py -s xxxx.md -t xxxx.html"
    print "-h      --help                                          - usage help of markup.py"
    print "-s      --source=source_file                  - source file which need handler."
    print "-t       --target=target_file                    - the html of  Processed output file"
    print
    print
    print "Examples: "
    print "python markup.py -s xxx.md"
    sys.exit(0)
    
    
def main():
    print "begin handler this week."
    global default_output_file
    global source_file
    global target_file
    
    try:
        opts,args=getopt.getopt(sys.argv[1:],"hs:t:",["help","source=","target="])
    except getopt.GetoptError as error:
        print str(error)
        usage()
    print "opts:%s" % str(opts)
    
    if not opts:
        usage()
    
    for opt,param in opts:
        if opt in ("-h","--help"):
            usage()
        elif opt in ("-s","--source="):
            if param:
                source_file=param
            else:
                usage()
        elif opt in    ("-t","--target="):
            if  param:
                default_output_file=False
                target_file=param
            else:
                usage()
        else:
            assert False,"Unhandled Option."
    print source_file
    if default_output_file:
        target_file="%s.html" % source_file[:str(source_file).rindex('.')]
        
    with codecs.open(source_file,encoding='utf-8',mode='r') as input_file:
        with codecs.open(target_file,encoding='utf-8',mode='w') as output_file:
            handler=HTMLRenderer(input_file,output_file)
            parse = BasicTextParser(handler)
            parse.parse(input_file)            
            
            
    
    
    
    
    



#start_log()
if __name__ == '__main__':
    print "this is main program."
    if not len(sys.argv[1:]):
            usage()
    else:
        main()
    #stop_log()















        
