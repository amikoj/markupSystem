#!/usr/bin/python
# -*- encoding:utf-8 -*-
'''
this file is the util of text plain creator.
'''


def lines(file):
    '''
    这个方法是逐行读取文件中的文本并且在文本最后添加一个空行.
    '''
    for line in file:
        yield line
    yield '\n'


def blocks(file):
    '''
    本方法是通过空行将文本分割为逐个文本块。
    '''
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ' '.join(block).strip()
            block = []
