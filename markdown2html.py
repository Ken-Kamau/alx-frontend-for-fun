#!/usr/bin/python3
"""
Markdown to HTML Script
"""
import os
import sys
import re
import markdown

def convert_markdown_to_html(markdown_file, output_file):
    """
    Conversion ofa markdown file to HTML file before saving the output_file

    :param markdown_file: Location of the markdown input file.
    :param output_file: Location of the HTML output file.
    """

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
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)
    sys.exit(0)
