import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("h1", "Welcome to my website!", {"href": "https://www.google.com"})
        node2 = LeafNode("h1", "Welcome to my website!", {"href": "https://www.google.com"})
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = LeafNode("h2", "Welcome to my website", {"href": "http://www.google.com"})
        node2 = LeafNode("h1", "Welcome to my website!", {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

    def test_to_html(self):
        node = LeafNode("h1", "Welcome to my website!", {"href": "https://www.google.com"})
        self.assertToHTML(node)

    def test_to_html_no_props(self):
        node = LeafNode("h1", "Welcome to my website!")
        self.assertToHTMLNoProps(node)


    def assertEqual(self, node, node2):
        if node.__eq__(node2) == True:
            return True
        raise Exception("Assert Equal Failed")
    
    def assertNotEqual(self, node, node2):
        if node.tag != node2.tag and node.value != node2.value and node.props != node2.props:
            return True
        raise Exception("Assert Not Equal Failed")
    
    def assertToHTML(self, node):
        html_result = node.to_html()
        if html_result == '<h1 href= "https://www.google.com">Welcome to my website!</h1>':
            return True
        raise Exception("Assert To HTML Failed")
    
    def assertToHTMLNoProps(self, node):
        if node.to_html() == "<h1>Welcome to my website!</h1>":
            return True
        raise Exception("Assert to HTML No Props Failed")

