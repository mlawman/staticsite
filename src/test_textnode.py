import unittest

from textnode import TextNode, TextType
from htmlutils import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node url test", TextType.LINK)
        node2 = TextNode("This is a text node url test", TextType.LINK, "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node url test", TextType.LINK, "https://boot.dev")
        node2 = TextNode("This is a text node url test", TextType.LINK, "https://boot.dev")
        self.assertEqual(node, node2)

    def test_split_with_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
])

    def test_split_with_bold(self):
        node = TextNode("The following text is **bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
    TextNode("The following text is ", TextType.TEXT),
    TextNode("bold", TextType.BOLD)
])

    def test_split_multiple_inputs_some_bold(self):
        node1 = TextNode("The following text is **bold**", TextType.TEXT)
        node2 = TextNode("Just some plain text.", TextType.TEXT)
        node3 = TextNode("Here is some _italic_ text.", TextType.TEXT)
        node4 = TextNode("Here's some more **bold text**, and that's it.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2, node3, node4], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
    TextNode("The following text is ", TextType.TEXT),
    TextNode("bold", TextType.BOLD),
    TextNode("Just some plain text.", TextType.TEXT),
    TextNode("Here is some _italic_ text.", TextType.TEXT),
    TextNode("Here's some more ", TextType.TEXT),
    TextNode("bold text", TextType.BOLD),
    TextNode(", and that's it.", TextType.TEXT),
])


if __name__ == "__main__":
    unittest.main()
