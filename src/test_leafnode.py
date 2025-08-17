import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_with_props_to_html(self):
        node = LeafNode("a", "This is a link", {
            "href": "https://www.bing.com",
            "target": "_blank",
            })
        expected = '<a href="https://www.bing.com" target="_blank">This is a link</a>'
        self.assertEqual(node.to_html(), expected)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        expected = "<p>Hello, world!</p>"
        self.assertEqual(node.to_html(), expected)

    def test_leaf_to_html_value_no_tag(self):
        node = LeafNode(None, "Just a value here")
        expected = "Just a value here"
        self.assertEqual(node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()
