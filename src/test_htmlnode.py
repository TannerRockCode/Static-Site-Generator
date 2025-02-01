import unittest 

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "Visit Oregon!", ["p", "a"], {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("h1", "Visit Oregon!", ["p", "a"], {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("h", "Visit Oregon!", ["p", "a"], {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("h1", "Visit Oregon!", ["p", "a"], {"href": "https://www.google.com","target": "_blank",})
        self.assertNotEqual(node, node2)

    def test_eq_attributes(self):
        node = HTMLNode("p", "Visit Oregon", ["a"], {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("h1", "Visit Oregon!", ["p", "a"], {"href": "https://www.google.com","target": "_blank",})
        self.assertEqualAttributes(node, node2)

    def test_not_eq_attributes(self):
        node = HTMLNode("h1", "Visit Oregon!", ["p", "a"], {"href": "https://www.hehe.com","target": "_blank",})
        node2 = HTMLNode("h1", "Visit Oregon!", ["p", "a"], {"href": "https://www.google.com","target": "_blank",})
        self.assertNotEqualAttributes(node, node2)

    def assertEqual(self, node, node2):
        if node.__eq__(node2) == True:
            return True
        raise Exception("Failed Test")
    
    def assertNotEqual(self, node, node2):
        if node.__eq__(node2) == False:
            return True
        raise Exception("Failed Test")
    
    def assertEqualAttributes(self, node, node2):
        if (node.props == node2.props):
            return True 
        raise Exception("Failed Test")
    
    def assertNotEqualAttributes(self, node, node2):
        if (node.props != node2.props):
            return True 
        raise Exception("Failed Test")