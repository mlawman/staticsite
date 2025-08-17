import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_output(self):
        node = HTMLNode(props={
            "href": "https://www.bing.com",
            "target": "_blank",
            })
        expected = ' href="https://www.bing.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_without_params_returns_empty_string_for_props_html(self):
        node = HTMLNode()
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

    def test_prop_without_value_output(self):
        node = HTMLNode(props={"test": ""})
        expected = ' test=""'
        self.assertEqual(node.props_to_html(), expected)

if __name__ == "__main__":
    unittest.main()
