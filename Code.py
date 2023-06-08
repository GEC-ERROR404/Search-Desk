import time
import os
import cv2
import pytesseract
from typing import Tuple
from io import BytesIO
import argparse
import re
import fitz

def searchtext(keyword):
    root = 'D:\\dataset'
    filenames = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            filenames.append(os.path.join(path, name))
    t1 = time.time()
    for file_name in filenames:
        if(".txt" in file_name):
            with open(file_name, 'r', encoding='utf-8') as f:
                data = f.read()
                words = keyword.split()
                for w in words:
                    if w in data:
                        Count = data.count(w)
                        final_path = file_name
                        print(w," word found ",Count,"times in this path ",final_path)
    t2 = time.time()
    print("time taken for text files", t2 - t1)
    t1 = time.time()
    for file_name in filenames:
        if(".doc" in file_name or ".docx" in file_name):
            with open(file_name, 'r', encoding='ISO-8859-1') as f:
                data = f.read()
                words = keyword.split()
                for w in words:
                    if w in data:
                        Count = data.count(w)
                        final_path = file_name
                        print(w," word found ",Count,"times in this path ",final_path)
    t2 = time.time()
    print("time taken for document files", t2 - t1)
    t1 = time.time()
    for file_name in filenames:
        if(".jpg" in file_name or ".png" in file_name or ".jpeg" in file_name):
            img = cv2.imread(file_name)

            # Adding custom options
            custom_config = r'--oem 3 --psm 6'
            data=pytesseract.image_to_string(img, config=custom_config)
            words = keyword.split()
            for w in words:
                if w in data:
                    Count = data.count(w)
                    final_path = file_name
                    print(w," word found ",Count,"times in this path ",final_path)
    t2 = time.time()
    print("time taken for image files", t2 - t1)
    for file_name in filenames:
        if(".pdf" in file_name):
            pdfDoc = fitz.open(file_name)
            output_buffer = BytesIO()
            total_matches = 0
            text = ""
            for pg in range(pdfDoc.page_count):
                page = pdfDoc[pg]
            lines = page.get_text("text").split('\n')
            for w in words:
                for line in lines:
                    if(re.findall(w, line, re.IGNORECASE)):
                        break
                Count = data.count(w)
                final_path = file_name
                print(w," word found ",Count,"times in this path ",final_path)
    pass

searchtext("machine")