import unittest 

from textnode import TextNode, TextType 
from leafnode import LeafNode

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

    def test_text_node_type_text_to_html_node(self):
        node = TextNode("Text Type", TextType.TEXT)
        self.assertTypeTextToHtmlNode(node)

    def test_text_node_type_bold_to_html_node(self):
        node = TextNode("Bold Type", TextType.BOLD)
        self.assertTypeBoldToHtmlNode(node)

    def test_text_node_type_italic_to_html_node(self):
        node = TextNode("Italic Type", TextType.ITALIC)
        self.assertTypeItalicToHtmlNode(node)

    def test_text_node_type_code_to_html_node(self):
        node = TextNode("Code Type", TextType.CODE)
        self.assertTypeCodeToHtmlNode(node)

    def test_text_node_type_link_to_html_node(self):
        node = TextNode("Link Type", TextType.LINK, {"href": "https://google.com"})
        self.assertTypeLinkToHtmlNode(node)

    def test_text_node_type_image_to_html_node(self):
        node = TextNode("", TextType.IMAGE, {"src": "/home/tanner/repos/static-site/static/images/rivendell.png", "alt": "Image of Riverdell"})
        self.assertTypeImageToHtmlNode(node)

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
    
    def assertTypeTextToHtmlNode(self, node):
        html_node = node.text_node_to_html_node().to_html()
        expected_result = LeafNode(None, node.text).to_html()
        if html_node != expected_result:
            raise Exception("Type Text To Html Node did not return expected result")
        
    def assertTypeBoldToHtmlNode(self, node):
        html_node = node.text_node_to_html_node().to_html()
        expected_result = LeafNode("b", node.text).to_html()
        if html_node != expected_result:
            raise Exception("Type Bold To Html Node did not return expected result")
    
    def assertTypeItalicToHtmlNode(self, node):
        html_node = node.text_node_to_html_node().to_html()
        expected_result = LeafNode("i", node.text).to_html()
        if html_node != expected_result:
            raise Exception("Type Italic To Html Node did not return expected result")
        
    def assertTypeCodeToHtmlNode(self, node):
        html_node = node.text_node_to_html_node().to_html()
        expected_result = LeafNode("code", node.text).to_html()
        if html_node != expected_result:
            raise Exception("Type Code To Html Node did not return expected result")
        
    def assertTypeLinkToHtmlNode(self, node):
        html_node = node.text_node_to_html_node().to_html()
        expected_result = LeafNode("a", node.text, {"href": "https://google.com"}).to_html()
        if html_node != expected_result:
            raise Exception("Type Link To Html Node did not return expected result")
        
    def assertTypeImageToHtmlNode(self, node):
        html_node = node.text_node_to_html_node().to_html()
        expected_result = LeafNode("img", node.text, {"src": "/home/tanner/repos/static-site/static/images/rivendell.png", "alt": "Image of Riverdell"}).to_html()
        if html_node != expected_result:
            raise Exception("Type Link To Html Node did not return expected result")


if __name__ == "__main__":
    unittest.main()