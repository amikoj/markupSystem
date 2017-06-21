# /usr/bin/python
# -*- encoding:utf-8 -*-

class Rule:
    '''
     the basic class of all rules.
    '''
    def action(self,block,handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True
    
class HeadingRule(Rule):
    '''
    titile has only one line,and the most of 70 characters of title.end of ':' is error for title.
    '''
    type= 'heading'
    def condition(self,block):
        return not '\n' in block and len(block) <=70 and not block[-1] == ':'
    
    
class TitleRule(HeadingRule):
    '''
    title is the first block of text.
    '''
    type='title'
    first=True
    def condition(self,block):
        if not self.first:
            return False
        self.first=False
        return HeadingRule.condition(self,block)
    
    
class ListItemRule(Rule):
    '''
    list item 
    '''
    type='listitem'
    def condition(self,block):
        return block[0] == '-'
    
    def action(self,block,handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True
    
class ListRule(ListItemRule):
    type='list'
    inside=False
    def condition(self,block):
        return True
    def action(self,block,handler):
        if not self.inside and ListItemRule.condition(self,block):
            handler.start(self.type)
            self.inside=True
        elif self.inside and not ListItemRule.condition(self,block):
            handler.end(self.type)
            self.inside=False
        return False
    
class ParagraphRule(Rule):
    '''
    content of text.
    '''
    type='paragraph'
    def condition(self,block):
        return True
    
    

        