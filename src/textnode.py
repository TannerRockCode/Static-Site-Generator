from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "Text"
    BOLD = "Bold"
    ITALIC = "Italic"
    CODE = "Code"
    LINK = "Link"
    IMAGE = "Image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text 
        self.text_type = text_type
        self.url = url 

    def __eq__(self, text_Node2):
        if self.text == text_Node2.text and self.text_type == text_Node2.text_type and self.url == text_Node2.url:
            return True
        return False
    
    def __repr__(self):
        return "TextNode({text}, {text_type}, {url})".format(text = self.text, text_type = self.text_type, url = self.url)

    
    def text_node_to_html_node(self):
        match self.text_type:
            case TextType.TEXT:
                node = LeafNode(None, self.text)
                return node
            case TextType.BOLD:
                node = LeafNode("b", self.text)
                return node
            case TextType.ITALIC:
                node = LeafNode("i", self.text)
                return node
            case TextType.CODE:
                node = LeafNode("code", self.text)
                return node
            case TextType.LINK:
                node = LeafNode("a", self.text, self.url)
                return node
            case TextType.IMAGE:
                node = LeafNode("img", "", self.url)
                return node
            case _:
                raise Exception("TextType given by text node does not exist as defined TextType")
                return
            
        
