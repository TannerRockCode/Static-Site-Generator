class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value 
        self.children = children 
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        all_html_str = ""
        prop_copy = self.props
        for key, value in prop_copy.items():
            cur_html_str = ('{k}= "{v}"').format(k = key, v = value)
            all_html_str =  all_html_str + " " + cur_html_str 
        return all_html_str
    
    def __repr__(self):
        if self.tag != None and self.children != None and self.value == None and self.props == None:
            return f"Tag: {self.tag} Children: {self.children}"
        if self.tag != None and self.value != None and self.children == None and self.props == None:
            return f"Tag: {self.tag} Value: {self.value}"
        if self.tag != None and self.value == None and self.children == None and self.props == None:
            return f"Tag: {self.tag}"
        return f"Tag: {self.tag} Value: {self.value} Children: {self.children} Props: {self.props}"

    def __eq__(self, node2):
        if (self.tag == node2.tag and self.value == node2.value and self.children == node2.children and self.props == node2.props):
            return True 
        return False
    