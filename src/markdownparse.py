from textnode import TextNode, TextType
import re

class MarkDownParse:
    def __init__(self):
        self

    def extract_markdown_images(self, text):
        split_text_list = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
        return split_text_list
    
    def extract_markdown_links(self, text):
        split_text_list = re.findall(r"\[(.*?)\]\((.*?)\)", text)
        return split_text_list
    
    def split_markdown_images(self, old_node):
        new_nodes_list = []
        split_text_list = re.split(r"\!\[(.*?)\]\((.*?)\)", old_node.text)
        image_text = ""
        image_prop = ""

        if len(split_text_list) == 1:
            return [old_node]
        
        for index, value in enumerate(split_text_list):
            if value == '':
                continue
            if index % 3 == 0:
                new_node = TextNode(value, old_node.text_type)
                new_nodes_list.append(new_node) 
            if index % 3 == 1: 
                image_text = value 
                image_type = TextType.IMAGE 
            if index % 3 == 2:
                image_prop = value
                new_node = TextNode(image_text, image_type, image_prop)
                image_text = ""
                image_type = ""
                new_nodes_list.append(new_node)
        return new_nodes_list
    
    def split_markdown_links(self, old_node):
        new_nodes_list = []
        split_text_list = re.split(r"\[(.*?)\]\((.*?)\)", old_node.text)
        link_text = ""
        link_prop = ""
        if len(split_text_list) == 1:
            return [old_node]
        for index, value in enumerate(split_text_list):
            if value == '':
                continue
            if index % 3 == 0:
                new_node = TextNode(value, old_node.text_type)
                new_nodes_list.append(new_node)
            if index % 3 == 1: 
                link_text = value 
                link_type = TextType.LINK
            if index % 3 == 2:
                link_prop = value
                new_node = TextNode(link_text, link_type, link_prop)
                link_text = ""
                link_type = ""
                new_nodes_list.append(new_node)
        return new_nodes_list

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
        #print(f"old_nodes: {old_nodes} delimiter: {delimiter} text_type: {text_type}")
        for old_node in old_nodes:
            #print(f"old_node: {old_node}")
            old_node_parts = old_node.text.split(delimiter)
            #print(f"old_nodes: {old_nodes} delimiter: {delimiter} text_type: {text_type}")
            #print(f"old_node_parts: {old_node_parts}")
            if len(old_node_parts) % 2 == 0:
                raise Exception("SplitNodeDelimiter: Odd number of delimiters - missing delimiter")
            new_sub_nodes = self.parse_delimiter_text(old_node_parts, old_node, delimiter, text_type)
            new_nodes.extend(new_sub_nodes)
        
        return new_nodes
    
    def split_nodes_image(self, old_nodes):
        new_nodes_list = []
        for old_node in old_nodes:
            split_images_list = self.split_markdown_images(old_node)
            new_nodes_list.extend(split_images_list)
        return new_nodes_list
            
    def split_nodes_link(self, old_nodes):
        new_nodes_list = []
        for old_node in old_nodes:
            split_links_list = self.split_markdown_links(old_node)
            new_nodes_list.extend(split_links_list)
        return new_nodes_list
    
    def text_to_textnodes(self, text):
        orig_node = TextNode(text, TextType.TEXT)
        orig_nodes_w_code = self.split_nodes_delimiter([orig_node], "`", TextType.CODE)
        orig_nodes_w_bold = self.split_nodes_delimiter(orig_nodes_w_code, "**", TextType.BOLD) 
        orig_nodes_w_italic = self.split_nodes_delimiter(orig_nodes_w_bold, "*", TextType.ITALIC)
        orig_nodes_w_images = self.split_nodes_image(orig_nodes_w_italic)
        orig_nodes_w_links = self.split_nodes_link(orig_nodes_w_images)
        final_nodes = orig_nodes_w_links
        return final_nodes

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
            
        
