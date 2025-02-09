from markdownparse import MarkDownParse
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode
import re

class BlockMarkDownParse:
    def __init__(self):
        self

    def extract_title(self, markdown):
        markdown_blocks = self.markdown_to_blocks(markdown)
        for block in markdown_blocks:
            if re.match("# ", block):
                block = block.strip('#')
                block = block.strip()
                return block
        raise Exception("ExtractTitle: Could not find h1 header.")

    def markdown_to_blocks(self, markdown):
        #print(f"markdown: {markdown}")
        markdown_lines = re.split(r'\n\s*\n|\r\n\s*\r\n', markdown)
        for i in range(len(markdown_lines)):
            markdown_lines[i] = markdown_lines[i].strip()
        return markdown_lines
    
    # def markdown_to_html_node(self, markdown):
    #     markdown_blocks = self.markdown_to_blocks(markdown)
    #     htmlNodeList = []
    #     for markdown_block in markdown_blocks:
    #         block_type = self.block_to_block_type(markdown_block)
    #         updated_block = self.remove_markdown_type(block_type, markdown_block)
    #         html_node = self.block_to_html_node(block_type, updated_block)
    #         html_node_parsed_inline = self.parse_inline_markdown(html_node)
    #         htmlNodeList.append(html_node_parsed_inline)
    #         #have a way to check if there are children! if there are children add children to html_node object.
    #         #otherwise just assign the existing html_node.value to html_node.value - no children to be added!
    #     finalHtmlNode = ParentNode("div", htmlNodeList)
    #     return finalHtmlNode
    
    def markdown_to_html_node(self, markdown):
        #print(f"Calling markdown_to_html_node: {repr(markdown)}")
        markdown_blocks = self.markdown_to_blocks(markdown)
        #print(f"markdown_blocks: {markdown_blocks}")
        htmlNodeList = []
        for markdown_block in markdown_blocks:
            block_type = self.block_to_block_type(markdown_block)
            updated_block = self.remove_markdown_type(block_type, markdown_block)
            #print(f"updated_block: {updated_block}")
            html_node = self.block_to_html_node(block_type, updated_block)
            #print(f"\nhtml_node: {html_node}\n")
            #print(f"html_node: {html_node}")
            html_node_parsed_inline = self.parse_inline_markdown(html_node)
            #print(f"html_node_parsed_inline: {html_node_parsed_inline}")
            htmlNodeList.append(html_node_parsed_inline)
            #have a way to check if there are children! if there are children add children to html_node object.
            #otherwise just assign the existing html_node.value to html_node.value - no children to be added!
        finalHtmlNode = ParentNode("div", htmlNodeList)
        #print(f"finalHtmlNode: {finalHtmlNode}")
        return finalHtmlNode

    #html_node = self.parse_block_children(html_node.tag, html_node.value)
    
    def block_to_html_node(self, block_type, markdown_block):
        if self.parent_block_type(block_type): #check if ul or ol 
            #print(f"Found parent block type in block_to_html_node! {block_type}")
            block_children = self.parse_block_parent_children(block_type, markdown_block)
            html_node = ParentNode(block_type, block_children)
            #dont return yet -  we want to process the text to children!
            return html_node
        else:
            html_node = ParentNode(block_type, markdown_block)
            #print(f"else parent node in block_to_html: {html_node}")
            #dont return yet -  we want to process the text to children!
            return html_node
        
    def parse_inline_markdown(self, html_node):
        if self.parent_block_type(html_node.tag):
            node_children = []
            for node_child in html_node.children:
                #print(f"node_child: {node_child}")
                #print(f"node_child.value: {node_child.value}")
                child_inline_nodes = self.text_to_children(node_child.value)
                #print(f"child_inline_nodes: {child_inline_nodes}")
                #print(f"node_child.tag: {node_child.tag}")
                html_node_w_inline = ParentNode(node_child.tag, child_inline_nodes)
                node_children.append(html_node_w_inline)
            html_node_w_inline_children = ParentNode(html_node.tag, node_children)
            #print(f"html_node_w_inline_children: {html_node_w_inline_children}")
            return html_node_w_inline_children
        else: 
            child_inline_nodes = self.text_to_children(html_node.value)
            html_node_w_inline = ParentNode(html_node.tag, child_inline_nodes)
            #print(f"non parent html_node_w_inline: {html_node_w_inline}")
            return html_node_w_inline
        
    def text_to_children(self, text):
        markdown = MarkDownParse()
        textnodes = markdown.text_to_textnodes(text) 
        leafnodes = []
        for text_node in textnodes:
            #print(f"text_node: {text_node}")
            leafnode = text_node.text_node_to_html_node()
            leafnodes.append(leafnode)
        #leafnodes = textnode.text_node_to_html_node(self)
        #print(f"Leafnodes: {leafnodes}")
        return leafnodes

    def parse_block_parent_children(self, block_type, markdown_block):
        match(block_type):
            case "ol":
                children = self.parse_block_list(markdown_block, block_type)
                return children
            case "ul":
                children = self.parse_block_list(markdown_block, block_type)
                return children
            case _:
                return None
        
    def parse_block_list(self, markdown_block, block_type):
        #insert /r/n to beginning of list so that list can be parsed by splitting on /r/n
        list_type = "li"
        #print(f"markdown_block: {repr(markdown_block)}")
        li_markdown_block = "\r\n" + markdown_block
        #add check for ul or ol to change parsing
        markdown_li_list = []
        if block_type == "ul":
            markdown_li_list = re.split(r'(?:\r\n|\n)\s*\*|\s*\-', li_markdown_block) #tanner this is what you have to fix
        if block_type == "ol":
            markdown_li_list = re.split(r'(?:\r\n|\n)\s*\d+.', li_markdown_block)
        #print(f"markdown_li_list: {markdown_li_list}")
        html_node_li_list = []
        for li in markdown_li_list:
            li = li.strip()
            if li == "" or li == '':
                continue
            li_node = ParentNode(list_type, li)
            html_node_li_list.append(li_node)
        
        #print(f"html node li list: {html_node_li_list}")
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
            case "blockquote":
                block = block.strip(">")
                return block.strip()
            # case "ul":
            #     return block.strip("* ")
            # case "ul":
            #     return block.strip("-")
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
            return "blockquote"
        if re.match("\* ", block):
            return "ul"
        if re.match("- ", block):
            return "ul"
        if re.match("\d. ", block):
            return "ol"
        else:
            return "p"
            
            

    

