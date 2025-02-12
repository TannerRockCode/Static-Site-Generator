import unittest

from generate_page import GeneratePage

class TestGeneratePage(unittest.TestCase):

    def test_generate_page(self):
        generate_page = GeneratePage()
        generate_page.markdown_path
        generate_page.template_path
        generate_page.destination_path
        self.assertGeneratePage(generate_page, generate_page.markdown_path, generate_page.template_path, generate_page.destination_path)

    def test_generate_pages_recursive(self):
        generate_page = GeneratePage()
        generate_page.markdown_path
        generate_page.template_path
        generate_page.destination_path
        self.assertGeneratePageRecursively(generate_page, generate_page.content_path, generate_page.template_path, generate_page.destination_path)


    def assertGeneratePage(self, generate_page, from_path, template_path, dest_path):
        result = generate_page.generate_page(from_path, template_path, dest_path)
        #result = generate_page.generate_pages_recursive(from_path, template_path, dest_path)
        #print(f"result: {result}")

    def assertGeneratePageRecursively(self, generate_page, from_path, template_path, dest_path):
        result = generate_page.generate_pages_recursive(from_path, template_path, dest_path)

    