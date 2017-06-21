# /usr/bin/python
# -*- encoding:utf-8 -*-

'''
a simple markup programing
'''

import sys,re


from util import *
print '<html><head> <title> Test txt</title><body>'
title =True
#可以通过命令 ‘<’指定输入源，re为python中的正则表达模块
for block in blocks(sys.stdin):
    #该正则是表示将*txt*的文本添加<em>text</em>标签(斜体)
    block =re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title=False
    else:
        print '<p>'
        print block
        print '</p>'
print '</body>\n</html>'
