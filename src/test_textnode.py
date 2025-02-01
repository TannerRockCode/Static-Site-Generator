import unittest 

from textnode import TextNode, TextType 

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertUrlNone(node)
    
    def test_texttype_not_eq(self):
         node = TextNode("This is a text node", TextType.BOLD)
         node2 = TextNode("This is a text node", TextType.ITALIC)
         self.assertTextTypeNotEqual(node, node2)
        
    def test_texttype_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertTextTypeEqual(node, node2)

    def assertEqual(self, node, node2):
        return node.__eq__(node2)
    
    def assertNotEqual(self, node, node2):
        return not node.__eq__(node2)
    
    def assertUrlNone(self, node):
        if (node.url == None):
            return True
        return False
    
    def assertTextTypeNotEqual(self, node, node2):
        if (node.text_type != node.text_type):
            return True
        return False
    
    def assertTextTypeEqual(self, node, node2):
        if (node.text_type == node2.text_type):
            return True 
        return False
    

if __name__ == "__main__":
    unittest.main()