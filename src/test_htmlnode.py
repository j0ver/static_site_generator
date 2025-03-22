import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_default_to_none(self):
        node = HTMLNode()
        node2 = HTMLNode(None, None, None, None)
        self.assertEqual(node, node2)

    def test_eq(self):
        child1 = HTMLNode()
        child2 = HTMLNode()
        node = HTMLNode("h1", "some text", [child1,child2], {"href": "https://www.google.com"})
        node2 = HTMLNode("h1", "some text", [child1,child2], {"href": "https://www.google.com"})
        self.assertEqual(node, node2)
    
    def test_diff_tag(self):
        child1 = HTMLNode()
        child2 = HTMLNode()
        node = HTMLNode("h1", "some text", [child1,child2], {"href": "https://www.google.com"})
        node2 = HTMLNode("p", "some text", [child1,child2], {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)
        
    def test_diff_value(self):
        child1 = HTMLNode()
        child2 = HTMLNode()
        node = HTMLNode("h1", "some text", [child1,child2], {"href": "https://www.google.com"})
        node2 = HTMLNode("h1", "some different text", [child1,child2], {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

    def test_diff_no_children(self):
        child1 = HTMLNode()
        child2 = HTMLNode()
        child3 = HTMLNode()
        node = HTMLNode("h1", "some text", [child1,child2], {"href": "https://www.google.com"})
        node2 = HTMLNode("p", "some text", [child1,child2,child3], {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

    def test_diff_children(self):
        child1 = HTMLNode()
        child2 = HTMLNode()
        child3 = HTMLNode()
        node = HTMLNode("h1", "some text", [child1,child2], {"href": "https://www.google.com"})
        node2 = HTMLNode("p", "some text", [child1,child3], {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

    def test_diff_props(self):
        child1 = HTMLNode()
        child2 = HTMLNode()
        node = HTMLNode("h1", "some text", [child1,child2], {"href": "https://www.google.com"})
        node2 = HTMLNode("h1", "some text", [child1,child2], {"href": "https://www.bing.com"})
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()