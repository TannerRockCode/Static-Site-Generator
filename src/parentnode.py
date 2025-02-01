from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, children, props)
        self.tag = tag
        self.children = children
        self.props = props
    
    def to_html(self):
        if self is None:
            return ""
        if self.tag is None:
            raise ValueError("object cannot have missing tag")
            return ""
        if self.children is None:
            raise ValueError("object cannot have missing children")
            return ""
       
        final_html = f"<{self.tag}>"
        for child in self.children:
            final_html = final_html + child.to_html()
        final_html += f"</{self.tag}>"
        return final_html

        

