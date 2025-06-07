from textnode import *
from htmlnode import *

def main():
    node = TextNode("sometext", "link", "thisisan.url")
    print(node)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        elif delimiter not in ["**", "_", "`", "[", "![", "]"]:
            raise Exception("unknown text delimiter")
        else:
            

main()