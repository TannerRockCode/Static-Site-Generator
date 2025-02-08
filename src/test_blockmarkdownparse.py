import unittest 

from blockmarkdownparse import BlockMarkDownParse
from htmlnode import HTMLNode
from textnode import TextNode, TextType

class TestBlockMarkDown(unittest.TestCase):

    def test_markdown_blocks_to_html_nodes_all(self):
        input_string = "# This is a heading\r\n\r\n This is a paragraph of text. It has some **bold** and *italic* words inside of it.\r\n\r\n* This is the first list item in a list block\r\n* This is a list item\r\n* This is another list item"
        self.assertMarkdownBlocksToHtmlNodesAll(input_string)

    def test_markdown_to_blocks_all(self):
        input_string = "# This is a heading\r\n\r\n This is a paragraph of text. It has some **bold** and *italic* words inside of it.\r\n\r\n* This is the first list item in a list block\r\n* This is a list item\r\n* This is another list item"
        self.assertMarkdownToBlocksAll(input_string)

    def test_markdown_block_to_block_type_heading(self):
        input_block = '# This is a heading'
        self.assertMarkdownBlockToBlockTypeHeading(input_block)

    def test_markdown_block_to_block_type_list(self):
        input_block = '1. This is a ordered list element'
        self.assertMarkdownBlockToBlockTypeOrderedList(input_block)

    def assertMarkdownToBlocksAll(self, input_string):
        block_markdown = BlockMarkDownParse()
        result = block_markdown.markdown_to_blocks(input_string)
        expected_result = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\r\n* This is a list item\r\n* This is another list item']
        if result != expected_result:
            raise Exception("AssertMarkdownToBlocksAll: Result did not return expected value!")

#tanner this is where you left off
    def assertMarkdownBlocksToHtmlNodesAll(self, input_string):
        block_markdown = BlockMarkDownParse()
        initial_html_nodes_list = block_markdown.markdown_blocks_to_html_node(input_string)
        #initial_result_before_parse_inline_markdown = HTMLNode("div", None, [HTMLNode("h1", 'This is a heading'), HTMLNode("p", 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.'), HTMLNode("ul", None, [HTMLNode('li', 'This is the first list item in a list block'), HTMLNode('li', 'This is a list item'),  HTMLNode('li', 'This is another list item')])])
        expected_result = HTMLNode("div", None, [HTMLNode("h1", None, [TextNode('This is a heading', TextType.TEXT, None)]), HTMLNode("p", None, [TextNode('This is a paragraph of text. It has some ', TextType.TEXT, None), TextNode('bold', TextType.BOLD, None), TextNode(' and ', TextType.TEXT, None), TextNode('italic', TextType.ITALIC, None), TextNode(' words inside of it.', TextType.TEXT, None)]), HTMLNode("ul", None, [HTMLNode('li', None, [TextNode('This is the first list item in a list block', TextType.TEXT, None)]), HTMLNode('li', None, [TextNode('This is a list item', TextType.TEXT, None)]),  HTMLNode('li', None, [TextNode('This is another list item', TextType.TEXT, None)])])])
        result = initial_html_nodes_list
        if result != expected_result:
            raise Exception("AssertMarkdownToHtmlNodesAll: Result did not return expected value!")
        
    def assertMarkdownBlockToBlockTypeHeading(self, input_block):
        block_markdown = BlockMarkDownParse()
        result = block_markdown.block_to_block_type(input_block)
        expected_result = "h1"

    def assertMarkdownBlockToBlockTypeOrderedList(self, input_block):
        block_markdown = BlockMarkDownParse()
        result = block_markdown.block_to_block_type(input_block)
        expected_result = "ol"

    
