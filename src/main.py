import os, shutil
from textnode import TextNode, TextType
print("Hello World")


def main():
    textnode = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(f"{textnode.__repr__()}")
    gen_site_files()

def gen_site_files():
    home_dir = "/home/tanner"
    src_dir = f"{home_dir}/repos/static-site/static"
    dest_dir = f"{home_dir}/repos/static-site/public"

    if os.path.exists(src_dir) == False:
        raise Exception("Source directory does not exist!")
    if os.path.exists(dest_dir) == False:
        raise Exception("Destination directory does not exist!")
    
    #delete all contents in the destination directory to ensure copy is clean
    clean_dest(dest_dir)

    #copy all contents from source directory to destination directory
    copy_src_to_dest(src_dir, dest_dir)

def copy_src_to_dest(src_dir, dest_dir, cur_path = ""):

    src_dir_list = os.listdir(src_dir)

    #print(f"Source directory: {src_dir}")
    #print(f"Source directory list: {src_dir_list}")
    for entry in src_dir_list:
        cur_entry_path = os.path.join(src_dir, entry)
        dest_entry_path = os.path.join(dest_dir, entry)
        #print(f"entry: {entry}")
        if os.path.isfile(cur_entry_path):
            #print(f"Entry is a file: {entry}")
            #copy file to destination
            shutil.copyfile(cur_entry_path, dest_entry_path)
            #verify file exists
            #print(f"Checking file location: {dest_entry_path}")
            if not os.path.exists(dest_entry_path):
                raise Exception(f"Failed to copy file {entry} to {dest_dir}")

        if os.path.isdir(cur_entry_path):
            #make directory at destination before recursion
            #print(f"Attempting to make directory at destination: {dest_entry_path}")
            os.mkdir(dest_entry_path, mode=0o755)
            if not os.path.exists(dest_entry_path):
                raise Exception(f"Failed to create directory {entry} in {dest_dir}")
            #recursively call copy_src_to_dest
            copy_src_to_dest(cur_entry_path, dest_entry_path)
    return

def clean_dest(dest_dir, parent_path = "", is_dir = False):
    dest_dir_list = os.listdir(dest_dir)
    if len(dest_dir_list) == 0:
        #print(f"Destination Directory is empty do not need to clear contents")
        return  

    #print(f"Destination Directory List: {dest_dir_list}")

    for entry in dest_dir_list:
        path = os.path.join(dest_dir, entry)
        #print(f"Clean destination path: {path}")
        if os.path.isfile(path):
            os.remove(path)
            #print(f"{path} has been successfully removed")
        if os.path.isdir(path):
            clean_dest(path, dest_dir, True)
            path_list = os.listdir(path)
            if len(path_list) == 0:
                os.rmdir(path)
                #print(f"{path} has been successfully removed")
    return

#def extract_title(markdown):
    #print(f"extract title called")
    


main()