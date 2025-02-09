from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, props)
        self.tag = tag 
        self.value = value 
        self.props = props

    def add_attribute(self, attribute, attribute_value):
        if self.props == None:
            return "<{a}>{av}</{a}>".format(a = attribute, av = attribute_value)
        #print(f"self.props: {self.props}")
        props_str = super().props_to_html()
        #print(f"props_str: {props_str}")
        final_str = "<{a}{p}>{av}</{a}>".format(a = attribute, av = attribute_value, p = props_str)
        #print(f"final_str: {final_str}")
        return final_str
    
    def to_html(self):
        if self.tag == None:
            return self.value 
        return self.add_attribute(self.tag, self.value)