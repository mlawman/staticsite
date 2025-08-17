class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        props = ""
        for prop, value in self.props.items():
            props += f' {prop}="{value}"'
        return props

    def __repr__(self):
        children = ""
        for child in self.children:
            children += f"{child}\n"
        props = self.props_to_html()

        return f"tag: {self.tag}, value: {self.value}, children:\n{children},\nprops: {props}"

