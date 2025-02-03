import unittest 

from blockmarkdownparse import BlockMarkDownParse

class TestBlockMarkDown(unittest.TestCase):

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

    def assertMarkdownBlockToBlockTypeHeading(self, input_block):
        block_markdown = BlockMarkDownParse()
        result = block_markdown.block_to_block_type(input_block)
        expected_result = "h1"

    def assertMarkdownBlockToBlockTypeOrderedList(self, input_block):
        block_markdown = BlockMarkDownParse()
        result = block_markdown.block_to_block_type(input_block)
        expected_result = "ol"

    
