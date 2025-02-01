from enum import Enum

class TextType(Enum):
    NORMAL = "Normal"
    BOLD = "Bold"
    ITALIC = "Italic"
    CODE = "Code"
    LINKS = "Links"
    IMAGES = "Images"

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
        return "TextNode({text}, {text_type}, {url})".format(text = self.text, text_type = self.text_type.value, url = self.url)

    
     
