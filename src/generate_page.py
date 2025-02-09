from htmlnode import HTMLNode
from blockmarkdownparse import BlockMarkDownParse

class GeneratePage():

    home_dir = "/home/tanner"
    template_path =  f"{home_dir}/repos/static-site/template.html"
    markdown_path = f"{home_dir}/repos/static-site/content/index.md"
    destination_path = f"{home_dir}/repos/static-site/public/index.html"
    
    def __init__(self):
        self

    def generate_page(self, from_path, template_path, dest_path):
        #print(f"Generating page from {from_path} to {dest_path} using {template_path}")
        #Open file to object
        
        with open(from_path) as from_path_file_object:
            from_path_file_string = from_path_file_object.read()
        with open(template_path) as template_file_object:
            template_file_string = template_file_object.read()

        #print(f"from_path_file_string: {from_path_file_string}")
        #print(f"template_file_string: {template_file_string}")

        #convert markdown file to HTML string
        block_markdown = BlockMarkDownParse()
        html_nodes = block_markdown.markdown_to_html_node(from_path_file_string)
        #print(f"html_nodes: {html_nodes}")
        html_string = html_nodes.to_html()
        print(f"html_string: {html_string}")

        block_markdown = BlockMarkDownParse()
        title = block_markdown.extract_title(from_path_file_string)
        print(f"title: {title}")

        temp_file_string = template_file_string.replace("{{ Title }}", title)
        html_file_string = temp_file_string.replace("{{ Content }}", html_string)

        index_file = open(dest_path, "x")
        index_file.close()
        
        index_file = open(dest_path, "a")
        index_file.write(html_file_string)
        index_file.close()



