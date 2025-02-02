from textnode import TextNode, TextType
import re

class MarkDownParse:
    def __init__(self):
        self

    def extract_markdown_images(self, text):
        split_text_list = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
        #print(f"split_text_list: {split_text_list}")
        return split_text_list
    
    def extract_markdown_links(self, text):
        split_text_list = re.findall(r"\[(.*?)\]\((.*?)\)", text)
        return split_text_list

    def parse_delimiter_text(self, old_node_parts, old_node, delimiter, text_type):
        new_nodes_list = []
        for index, value in enumerate(old_node_parts):
            if value == '':
                continue
            if index % 2 == 0:
                node_type = old_node.text_type
                new_node = TextNode(value, node_type)
                new_nodes_list.append(new_node)
            else:
                node_type = text_type
                new_node = TextNode(value, node_type)
                new_nodes_list.append(new_node)
        return new_nodes_list

    def split_nodes_delimiter(self, old_nodes, delimiter, text_type):
        new_nodes = []
        
        for old_node in old_nodes:
            old_node_parts = old_node.text.split(delimiter)
            if len(old_node_parts) % 2 == 0:
                raise Exception("SplitNodeDelimiter: Odd number of delimiters - missing delimiter")
            new_sub_nodes = self.parse_delimiter_text(old_node_parts, old_node, delimiter, text_type)
            new_nodes.extend(new_sub_nodes)
        
        return new_nodes

    def get_mark_down_type(delimiter):
        match delimiter:
            case "**": 
                return TextType.BOLD 
            case "*":
                return TextType.ITALIC
            case "[link]":
                return TextType.LINK
            case "!":
                return TextType.IMAGE
            case "`":
                return TextType.CODE
            case _:
                return TextType.TEXT
            
        
