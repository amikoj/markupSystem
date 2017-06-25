# /usr/bin/python
# -*- encoding:utf-8 -*-

class Handler:
    '''
     处理程序
    '''
    def callback(self,prefix,name,*args):
        method = getattr(self,prefix+name,None)
        if callable(method):
            return method(*args)

    def start(self,name):
        self.callback('start_',name)

    def end(self,name):
        self.callback('end_',name)

    def sub(self,name):
        def substitution(match):
            result= self.callback('sub_',name,match)
            if result is None:
                result=match.group(0)
            return result
        return substitution


class HTMLRenderer(Handler):
    '''
    create html file .
    '''
    
    def __init__(self,input_file=None,output_file=None):
        if  input_file != None:
            self.input_file=input_file
        if  output_file !=None:
            self.output_file=output_file
        
        
    def start_document(self):
        self.output_file.write( '<html>\n<head>\n<title> ........</title>\n</head>\n<body>\n')

    def end_document(self):
        self.output_file.write( '</body>\n</html>')

    def start_paragraph(self):
        self.output_file.write( '<p>\n')

    def end_paragraph(self):
        self.output_file.write( '</p>\n')

    def start_heading(self):
        self.output_file.write( '<h2>\n')

    def end_heading(self):
        self.output_file.write( '</h2>\n')

    def start_list(self):
        self.output_file.write( '<ul>\n')

    def end_list(self):
        self.output_file.write( '</ul>\n')

    def start_listitem(self):
        self.output_file.write( '<li>\n')

    def end_listitem(self):
        self.output_file.write( '</li>\n')

    def start_title(self):
        self.output_file.write( '<h1>\n')

    def end_title(self):
        self.output_file.write( '</h1>\n')

    def sub_emphasis(self,match):
        return '<em>%s</em>' % match.group(1)

    def sub_url(self,match):
        return '<a href="%s">%s</a>' % (match.group(1),match.group(1))

    def sub_mail(self,match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1),match.group(1))

    def feed(self,data):
        self.output_file.write("%s\n" % data)
