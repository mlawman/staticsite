import re

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def markdown_to_blocks(markdown):
    blocks = []
    parts = markdown.split('\n\n')
    for part in parts:
        part = part.strip()
        if part != "":
            blocks.append(part.strip())
    return blocks