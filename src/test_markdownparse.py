import unittest 

from textnode import TextNode, TextType 
from markdownparse import MarkDownParse

class TestMarkDownParse(unittest.TestCase):
    
    def test_split_nodes_delimiter_two_bold(self):
        markdown = MarkDownParse()
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        node2 = TextNode("**This is text** with a bolded phrase in the beginning", TextType.TEXT)
        new_nodes = markdown.split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        self.assertSplitNodesDelimiterTwoBold(new_nodes)

    def test_split_nodes_delimiter_missing_one(self):
        node = TextNode("This is text with a bolded phrase** in the middle", TextType.TEXT)
        node2 = TextNode("**This is text with a bolded phrase in the beginning", TextType.TEXT)
        node3 = TextNode("This is text with a bolded phrase in the end**", TextType.TEXT)
        node_list = [node, node2, node3]
        self.assertSplitNodesDelimiterMissingOne(node_list)

    def assertSplitNodesDelimiterTwoBold(self, new_nodes):
        expected_nodes_list = [TextNode("This is text with a ", TextType.TEXT), TextNode("bolded phrase", TextType.BOLD), TextNode(" in the middle", TextType.TEXT), TextNode("This is text", TextType.BOLD), TextNode(" with a bolded phrase in the beginning", TextType.TEXT)]
        if new_nodes != expected_nodes_list:
            raise ValueError("Split Nodes Delimiter Two Bold test case did not return expected result")
    
    def assertSplitNodesDelimiterMissingOne(self, node_list):
        markdown = MarkDownParse()
        with self.assertRaises(Exception) as context:
            markdown.split_nodes_delimiter(node_list, "**", TextType.BOLD)
        self.assertIn("SplitNodeDelimiter: Odd number of delimiters - missing delimiter", str(context.exception))

    

        
           
    