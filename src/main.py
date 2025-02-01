import os
from textnode import TextNode, TextType
print("Hello World")


def main():
    textnode = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(f"{textnode.__repr__()}")
    copy_src_to_dest()

def copy_src_to_dest():
    home_dir = "/home/tanner"
    src_dir = f"{home_dir}/repos/static-site/static"
    dest_dir = f"{home_dir}/repos/static-site/public"

    if os.path.exists(src_dir) == False:
        raise Exception("Source directory does not exist!")
    if os.path.exists(dest_dir) == False:
        raise Exception("Destination directory does not exist!")
    
    #delete all contents in the destination directory to ensure copy is clean
    dest_dir_list = os.listdir(dest_dir)
    print(f"Destination Directory List: {dest_dir_list}")

    for entry in dest_dir_list:
        path = os.path.join(dest_dir, entry)
        os.remove(path)
        print(f"% has been successfully removed", entry)
    
    

main()