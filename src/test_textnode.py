import unittest

from textnode import TextNode, TextType

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


if __name__ == "__main__":
    unittest.main()
