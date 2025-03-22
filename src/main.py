from textnode import TextNode
from htmlnode import HTMLNode

def main():
    text_node = TextNode("This is some anchor text", "link", "https://boot.dev")
    html_node = HTMLNode("h1", "some text", None, {"href": "https://www.google.com"})
    print (repr(html_node))

main()
