from os import listdir, mkdir, makedirs
from os.path import isfile, isdir, join, exists, dirname
from pathlib import Path
from htmlnode import HTMLNode
from blockmarkdownparse import BlockMarkDownParse


class GeneratePage():

    home_dir = "/home/tanner"
    template_path =  f"{home_dir}/repos/static-site/template.html"
    markdown_path = f"{home_dir}/repos/static-site/content/index.md"
    destination_path = f"{home_dir}/repos/static-site/public/index.html"
    
    content_path = f"{home_dir}/repos/static-site/content/"
    destination_dir = f"{home_dir}/repos/static-site/public/"

    def __init__(self):
        self

    def generate_page(self, from_path, template_path, dest_path):
        print(f"Generating page from {from_path} to {dest_path} using {template_path}")
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
        #print(f"html_string: {html_string}")

        block_markdown = BlockMarkDownParse()
        title = block_markdown.extract_title(from_path_file_string)
        #print(f"title: {title}")

        temp_file_string = template_file_string.replace("{{ Title }}", title)
        html_file_string = temp_file_string.replace("{{ Content }}", html_string)

        #directory = dirname(dest_path)
        #makedirs(directory, exist_ok=True)

        print(f"Opening file at dest_path to write: {dest_path}")
        # Open and write in a single block using 'with'
        with open(dest_path, "w") as index_file:
            index_file.write(html_file_string)

        if isfile(dest_path):
            #with open(dest_path, 'w') as index_file:
            print(f"opening file at dest_path to write: {dest_path}")
            # index_file = open(dest_path, "w")
            # index_file.close()

            # index_file = open(dest_path, "a")
            # index_file.write(html_file_string)
            # index_file.close()
        else: 
            print(f"cannot write to file dest_path is not a file: {dest_path}")

    def generate_pages_recursive(self, dir_path_content, template_path, dest_dir_path):
        items = []
        print(f"directory path content: {dir_path_content}")
        if isdir(dir_path_content):
            print(f"dir_path_content is a directory")
            items = listdir(dir_path_content)

        if not items or items is None:
            return

        for item in items:
            print(f'item: {item}')
            cur_path = join(dir_path_content, item)
            #print(f"cur_path: {cur_path}")
            #print(f"performing isfile check")
            if isfile(cur_path) and item.endswith(".md"): #and extension is md
                #print(f"determined isfile and .md extension is true")
                #get destination path
                orig_relative_path = self.get_relative_path(self.content_path, cur_path)
                relative_path = orig_relative_path.replace(".md", ".html")
                #print(f"Got relative path!: {relative_path}")
                #get destination dir
                relative_dir = self.get_relative_directory(self.content_path, cur_path)
                #print(f"Got relative dir!: {relative_dir}")
                new_destination_dir = self.destination_dir + relative_dir
                new_destination_path = self.destination_dir + relative_path

                #create destination path
                #verify destination does not exist before creating tanner this is your next step!
                dir_exists = exists(new_destination_dir)
                #print(f"new_distination_dir: {new_destination_dir}")
                if not dir_exists:
                    mkdir(new_destination_dir, mode=0o777)
                    print(f"Supposedly created new dir at: {new_destination_dir}")
                #generate html 
                #update template file with generate values
                #generate new html file
                #save the file to public directory matching current path structure
                dest_path = dest_dir_path + relative_path
                #print(f"dest_path is file: {}")
                if isfile(cur_path):
                    print(f"detected cur_path is a file -calling generate page: {cur_path}")
                    self.generate_page(cur_path, self.template_path, new_destination_path)
                
            if isdir(cur_path):
                print(f"determined cur_path is directory is true")
                self.generate_pages_recursive(cur_path, template_path, dest_dir_path)
        return

    # def generate_pages_recursive(self, dir_path_content, template_path, dest_dir_path):
    #     if isdir(dir_path_content):
    #     items = listdir(dir_path_content)

    #     if not items or items is None:
    #         return

    #     for item in items:
    #         print(f'item: {item}')
    #         cur_path = join(dir_path_content, item)
    #         #print(f"cur_path: {cur_path}")
    #         #print(f"performing isfile check")
    #         if isfile(cur_path) and item.endswith(".md"): #and extension is md
    #             #print(f"determined isfile and .md extension is true")
    #             #get destination path
    #             orig_relative_path = self.get_relative_path(self.content_path, cur_path)
    #             relative_path = orig_relative_path.replace(".md", ".html")
    #             #print(f"Got relative path!: {relative_path}")
    #             #get destination dir
    #             relative_dir = self.get_relative_directory(self.content_path, cur_path)
    #             #print(f"Got relative dir!: {relative_dir}")
    #             new_destination_dir = self.destination_dir + relative_dir
    #             new_destination_path = self.destination_dir + relative_path

    #             #create destination path
    #             #verify destination does not exist before creating tanner this is your next step!
    #             dir_exists = exists(new_destination_dir)
    #             #print(f"new_distination_dir: {new_destination_dir}")
    #             if not dir_exists:
    #                 mkdir(new_destination_dir, mode=0o777)
    #                 print(f"Supposedly created new dir at: {new_destination_dir}")
    #             #generate html 
    #             #update template file with generate values
    #             #generate new html file
    #             #save the file to public directory matching current path structure
    #             dest_path = dest_dir_path + relative_path
    #             #print(f"dest_path is file: {}")
    #             if isfile(cur_path):
    #                 print(f"detected cur_path is a file -calling generate page: {cur_path}")
    #                 self.generate_page(cur_path, self.template_path, new_destination_path)
                
    #         if isdir(cur_path):
    #             print(f"determined cur_path is directory is true")
    #             self.generate_pages_recursive(cur_path, template_path, dest_dir_path)

    def get_relative_path(self, base_dir, current_dir):
        base_path = Path(base_dir).resolve()
        current_path = Path(current_dir).resolve()

        try:
            relative_path = current_path.relative_to(base_path)
            return str(relative_path)
        except ValueError:
            raise Exception("Unable to determine relative path")
        
    def get_relative_directory(self, base_dir, current_dir):
        base_path = Path(base_dir).resolve()
        current_path = Path(current_dir).resolve()

        if current_path.is_file():
            current_path = current_path.parent

        try:
            relative_path = current_path.relative_to(base_path)
            return str(relative_path)
        except ValueError:
            raise Exception("Unable to determine relative path")




