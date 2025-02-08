from markdownparse import MarkDownParse
from htmlnode import HTMLNode
import re

class BlockMarkDownParse:
    def __init__(self):
        self

    def markdown_to_blocks(self, markdown):
        #print(f"markdown: {markdown}")
        markdown_lines = markdown.split("\r\n\r\n")
        for i in range(len(markdown_lines)):
            markdown_lines[i] = markdown_lines[i].strip()
        return markdown_lines
    
    def markdown_blocks_to_html_node(self, markdown):
        markdown_blocks = self.markdown_to_blocks(markdown)
        htmlNodeList = []
        for markdown_block in markdown_blocks:
            block_type = self.block_to_block_type(markdown_block)
            updated_block = self.remove_markdown_type(block_type, markdown_block)
            html_node = self.block_to_html_node(block_type, updated_block)
            html_node_parsed_inline = self.parse_inline_markdown(html_node)
            htmlNodeList.append(html_node_parsed_inline)
            #have a way to check if there are children! if there are children add children to html_node object.
            #otherwise just assign the existing html_node.value to html_node.value - no children to be added!
        finalHtmlNode = HTMLNode("div", None, htmlNodeList)
        return finalHtmlNode

    #html_node = self.parse_block_children(html_node.tag, html_node.value)
    
    def block_to_html_node(self, block_type, markdown_block):
        if self.parent_block_type(block_type): #check if ul or ol 
            block_children = self.parse_block_parent_children(block_type, markdown_block)
            html_node = HTMLNode(block_type, None, block_children)
            #dont return yet -  we want to process the text to children!
            return html_node
        else:
            html_node = HTMLNode(block_type, markdown_block)
            #dont return yet -  we want to process the text to children!
            return html_node
        
    def parse_inline_markdown(self, html_node):
        if self.parent_block_type(html_node.tag):
            node_children = []
            for node_child in html_node.children:
                child_inline_nodes = self.text_to_children(node_child.value)
                html_node_w_inline = HTMLNode(node_child.tag, None, child_inline_nodes)
                node_children.append(html_node_w_inline)
            html_node_w_inline_children = HTMLNode(html_node.tag, None, node_children)
            return html_node_w_inline_children
        else: 
            child_inline_nodes = self.text_to_children(html_node.value)
            html_node_w_inline = HTMLNode(html_node.tag, None, child_inline_nodes)
            return html_node_w_inline
        
    def text_to_children(self, text):
        markdown = MarkDownParse()
        textnodes = markdown.text_to_textnodes(text) 
        return textnodes

    def parse_block_parent_children(self, block_type, markdown_block):
        match(block_type):
            case "ol":
                children = self.parse_block_list(markdown_block)
                return children
            case "ul":
                children = self.parse_block_list(markdown_block)
                return children
            case _:
                return None
        
    def parse_block_list(self, markdown_block):
        #insert /r/n to beginning of list so that list can be parsed by splitting on /r/n
        list_type = "li"
        li_markdown_block = "\r\n" + markdown_block
        markdown_li_list = li_markdown_block.split("\r\n*")
        html_node_li_list = []
        for li in markdown_li_list:
            if li == "":
                continue
            li = li.strip()
            li_node = HTMLNode(list_type, li)
            html_node_li_list.append(li_node)
        return html_node_li_list

    def block_remove_markdown(block_type, markdown_block):
        markdown_block.strip()

    def parent_block_type(self, block_type):
        parent_block_types = ["ol", "ul"]
        if block_type in parent_block_types:
            return True
        return False

    def remove_markdown_type(self, type, block):
        match(type):
            case "h6":
                block = block.strip("######")
                return block.strip()
            case "h5":
                block = block.strip("#####")
                return block.strip()
            case "h4":
                block = block.strip("####")
                return block.strip()
            case "h3":
                block = block.strip("###")
                return block.strip()
            case "h2": 
                block = block.strip("##")
                return block.strip()
            case "h1":
                block = block.strip("#")
                return block.strip()
            case "q":
                block = block.strip(">")
                return block.strip()
            #case "ul":
                #return block.strip("\*")
            #case "ul":
                #return block.strip("-")
            case "ol":
                block = block.strip("\d.")
                return block.strip()
            case "p":
                return block 
            case _:
                return block
    
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
            
            

    

