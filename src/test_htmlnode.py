import unittest
from htmlnode import HTMLNode
from textnode import TextNode, TextType
from htmlutils import text_node_to_html_node, split_nodes_image, split_nodes_link


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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_with_image_first(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) text and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" text and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_with_no_images(self):
        node = TextNode(
            "Text and more text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Text and more text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_split_nodes_link_with_link_first(self):
        node = TextNode(
            "[Link to boot dev](https://www.boot.dev) and another to [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Link to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and another to ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_split_nodes_link_with_no_links(self):
        node = TextNode(
            "Text and more text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Text and more text", TextType.TEXT),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()
