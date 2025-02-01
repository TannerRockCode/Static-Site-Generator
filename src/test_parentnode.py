import unittest 

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text")],)
        node2 = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text")],)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = ParentNode("p", [LeafNode("p", "Bold text"), LeafNode(None, "Normal text")],)
        node2 = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text")],)
        self.assertNotEqual(node, node2)

    def test_to_html_one_depth_children(self):
        node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")],)
        self.assertToHtmlOneDepthChildren(node)
    
    def test_to_html_two_depth_children(self):
        node = ParentNode("page", [LeafNode("h1", "Introduction"), ParentNode("div", [LeafNode("p", "First paragraph text"), LeafNode("p", "Second paragraph text")]), LeafNode("i", "italic text"), LeafNode(None, "Normal text")],)
        self.assertToHtmlTwoDepthChildren(node)

    #def test_to_html_three_depth_children(self):

    #def test_to_html_four_depth_children(self):

    def assertEqual(self, node, node2):
        if node.__eq__(node2) == True:
            return True
        raise Exception("ParentNode Assert Equal did not return expected result.")
    
    def assertNotEqual(self, node, node2):
        if node.__eq__(node2) == False:
            return True
        raise Exception("ParentNode Assert Equal did not return expected result.")


    def assertToHtmlOneDepthChildren(self, node):
        html_result = node.to_html()
        if html_result == "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>":
            return True
        print(f"Expected result: <p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        print(f"Actual result: {html_result}")
        raise Exception("assertToHtmlOneDepthChildren did not return expected output.")
    
    def assertToHtmlTwoDepthChildren(self, node):
        html_result = node.to_html()
        if html_result == "<page><h1>Introduction</h1><div><p>First paragraph text</p><p>Second paragraph text</p></div><i>italic text</i>Normal text</page>":
            return True
        print(f"Expected result: <page><h1>Introduction</h1><div><p>First paragraph text</p><p>Second paragraph text</p></div><b>Bold text</b>Normal text<i>italic text</i>Normal text</page>")
        print(f"Actual result: {html_result}")
        raise Exception("assertToHtmlTwoDepthChildren did not return expected output.")