from typing import Tuple
from io import BytesIO
import os
import argparse
import re
import fitz
def search_for_text(lines, search_str):
    """
    Search for the search string within the document lines
    """
    for line in lines:
        results = re.findall(search_str, line, re.IGNORECASE)
        for result in results:
            yield result
def highlight_matching_data(page, matched_values, type):
    """
    Highlight matching values
    """
    matches_found = 0
    # Loop throughout matching values
    for val in matched_values:
        matches_found += 1
        matching_val_area = page.search_for(val)
        # print("matching_val_area",matching_val_area)
        highlight = None
        if type == 'Highlight':
            highlight = page.add_highlight_annot(matching_val_area)
        highlight.update()
    return matches_found
def process_data(input_file: str, output_file: str, search_str: str, pages: tuple = None, action: str = 'Highlight'):
    """
    Process the pages of the PDF File
    """
    pdfDoc = fitz.open(input_file)
    output_buffer = BytesIO()
    total_matches = 0
    for pg in range(pdfDoc.page_count):
        if pages:
            if str(pg) not in pages:
                continue
        page = pdfDoc[pg]
        page_lines = page.get_text("text").split('\n')
        matched_values = search_for_text(page_lines, search_str)
        if matched_values:
            if action == 'Highlight':
                matches_found = highlight_matching_data(
                    page, matched_values, action)
            total_matches += matches_found
    print(f"{total_matches} Match(es) Found of Search String {search_str} In Input File: {input_file}")
    pdfDoc.save(output_buffer)
    pdfDoc.close()
    with open(output_file, mode='wb') as f:
        f.write(output_buffer.getbuffer())