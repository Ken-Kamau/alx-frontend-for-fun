#!/usr/bin/python3
"""
Markdown to HTML Script
"""
import os
import sys
import re

def convert_markdown_to_html(makrdown_file, output_file):
    if not os.path.isfile(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)

    with open(markdown_file, 'r') as file:
        markdown_text = file.read()

    html = markdown.markdown(markdown_text)

    with open(output_file, 'w') as file:
            file.write(html)

if __name__ == "__main__":
    """
    Script Entry Point.
    """
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)
    sys.exit(0)
