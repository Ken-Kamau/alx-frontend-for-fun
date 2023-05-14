#!/usr/bin/python3
"""
Markdown to HTML Script
"""
import os
import sys
import re

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


def parse_headings(markdown_text):
    """
    Parses headings in Markdown syntax and generates corresponding HTML.

    :param markdown_text: The Markdown text.
    :return: The HTML with replaced headongs.
    """
    lines = markdown_text.split('\n')
    html_lines = []

    for line in lines:
        if line.startswith('#'):
            heading_level = min(line.count('#'), 6)
            heading_text = line.strip('#').strip()
            html_lines.append(
                f'<h{heading_level}>{heading_text}</h{heading_level}>')
        else:
            html_lines.append(line)

    return '\n'.join(html_lines)

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
