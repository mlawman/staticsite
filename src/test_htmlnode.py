import unittest
from htmlnode import HTMLNode
from textnode import TextNode, TextType
from htmlutils import text_node_to_html_node 

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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_text(self):
        node = TextNode("This should be bold.", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This should be bold.")

    def test_italic_text(self):
        node = TextNode("This should be in italics.", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This should be in italics.")

    def test_code_text(self):
        node = TextNode("print('Hello, world!')", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('Hello, world!')")

    def test_link_text(self):
        node = TextNode("This should be a link", TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This should be a link")

    def test_image_text(self):
        node = TextNode(None, TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")

if __name__ == "__main__":
    unittest.main()
