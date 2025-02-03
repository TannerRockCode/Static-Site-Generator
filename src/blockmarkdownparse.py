from markdownparse import MarkDownParse
import re

class BlockMarkDownParse:
    def __init__(self):
        self

    def markdown_to_blocks(self, markdown):
        markdown_lines = markdown.split("\r\n\r\n")
        for i in range(len(markdown_lines)):
            markdown_lines[i] = markdown_lines[i].strip()
        return markdown_lines
    
    def block_to_block_type(self, block):
        #print(f"block: {block}")
        if re.match("######", block):
            return "h6"
        if re.match("#####", block):
            return "h5"
        if re.match("####", block):
            return "h4"
        if re.match("###", block):
            return "h3"
        if re.match("##", block):
            return "h2"
        if re.match("#", block):
            return "h1"
        if re.match(">", block):
            return "q"
        if re.match("\*", block):
            return "ul"
        if re.match("-", block):
            return "ul"
        if re.match("\d. ", block):
            return "ol"
        else:
            return "p"
            
            

    

