from enum import Enum

class TextType(Enum):
    TEXT = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, nodeText, textType, url=None):
        self.text = nodeText
        self.text_type = textType
        self.url = url

    def __eq__(self, comparison):
        return self.text == comparison.text and self.text_type == comparison.text_type and self.url == comparison.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


