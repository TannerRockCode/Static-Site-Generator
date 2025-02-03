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

    def test_extract_markdown_images(self):
        test_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertExtractMarkdownImages(test_text)

    def test_extract_markdown_links(self):
        test_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertExtractMarkdownLinks(test_text)

    def test_split_nodes_images(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)
        self.assertSplitNodesImages([node])

    def test_split_nodes_links(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        self.assertSplitNodesLinks([node])

    def test_text_to_nodes(self):
        orig_string = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertTextToTextNodes(orig_string)
        
    def assertSplitNodesDelimiterTwoBold(self, new_nodes):
        expected_nodes_list = [TextNode("This is text with a ", TextType.TEXT), TextNode("bolded phrase", TextType.BOLD), TextNode(" in the middle", TextType.TEXT), TextNode("This is text", TextType.BOLD), TextNode(" with a bolded phrase in the beginning", TextType.TEXT)]
        if new_nodes != expected_nodes_list:
            raise ValueError("Split Nodes Delimiter Two Bold test case did not return expected result")
    
    def assertSplitNodesDelimiterMissingOne(self, node_list):
        markdown = MarkDownParse()
        with self.assertRaises(Exception) as context:
            markdown.split_nodes_delimiter(node_list, "**", TextType.BOLD)
        self.assertIn("SplitNodeDelimiter: Odd number of delimiters - missing delimiter", str(context.exception))
    
    def assertExtractMarkdownImages(self, test_text):
        markdown = MarkDownParse()
        extracted_list_of_tuples = markdown.extract_markdown_images(test_text)
        expected_outcome = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        if extracted_list_of_tuples != expected_outcome:
            raise Exception("AssertExtractMarkDownImages did not return expected result!")
        
    def assertExtractMarkdownLinks(self, test_text):
        markdown = MarkDownParse()
        extracted_list_of_tuples = markdown.extract_markdown_links(test_text)
        expected_outcome = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        if extracted_list_of_tuples != expected_outcome:
            raise Exception("AssertExtractMarkDownLinks did not return expected result!")

    def assertSplitNodesImages(self, old_nodes):
        markdown = MarkDownParse()
        split_nodes = markdown.split_nodes_image(old_nodes)
        expected_result = [TextNode("This is text with a ", TextType.TEXT, None), TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"), TextNode(" and ", TextType.TEXT, None), TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),]
        if split_nodes != expected_result:
            raise Exception("AssertSplitNodesImages did not return expected result!")
        
    def assertSplitNodesLinks(self, old_nodes):
        markdown = MarkDownParse()
        split_nodes = markdown.split_nodes_link(old_nodes)
        expected_result = [TextNode("This is text with a link ", TextType.TEXT), TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"), TextNode(" and ", TextType.TEXT), TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),]
        if split_nodes != expected_result:
            raise Exception("AssertSplitNodesLinks did not return expected result!")
    
    def assertTextToTextNodes(self, orig_string):
        markdown = MarkDownParse()
        result = markdown.text_to_textnodes(orig_string)
        expected_result = [    TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),]
        
        if result != expected_result:
            raise Exception("AssertTextToTextNodes: result did not match expected output!")


        
           
    