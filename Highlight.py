import time
import os
import cv2
import pytesseract
import re
import fitz
from ConvertDOCX2PDF import Converter
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def searchtext(keyword):
    time1 = time.time()
    root = 'D:\\dataset'
    links = {}
    filenames = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            filenames.append(os.path.join(path, name))
    for file_name in filenames:
        if ".txt" in file_name:
            with open(file_name, 'r', encoding='utf-8') as f:
                data = f.read().casefold()
                words = keyword.casefold().split()
                for w in words:
                    if w in data:
                        Count = data.count(w)
                        links[file_name] = Count
                        with open("D:/Dataset/Cache/" + file_name[11:] + '.html', mode='wt', encoding='utf-8') as f:
                            f.write(data.replace(w, '<span><mark>{}</mark></span>'.format(w)))
    for file_name in filenames:
        if ".png" in file_name or ".jfif" in file_name:
            img = cv2.imread(file_name)
            custom_config = r'--oem 3 --psm 6'
            data = pytesseract.image_to_string(img, config=custom_config).casefold()
            words = keyword.casefold().split()
            for w in words:
                if w in data:
                    Count = data.count(w)
                    links[file_name] = Count
                    with open("D:/Dataset/Cache/" + file_name[11:] + '.html', mode='wt', encoding='utf-8') as f:
                        f.write(data.replace(w, '<span><mark>{}</mark></span>'.format(w)))
    for file_name in filenames:
        if ".pdf" in file_name:
            Count = 0
            pdfDoc = fitz.open(file_name)
            for pg in range(pdfDoc.page_count):
                page = pdfDoc[pg]
                lines = page.get_text("text").split('\n')
                words = keyword.split()
                for w in words:
                    for line in lines:
                        w1 = w.casefold()
                        line1 = line.casefold()
                        long = 'created with an evaluation copy of aspose.words.'
                        if long in line1 or line1 == 'please visit: https://products.aspose.com/words/' or line1 == 'evaluation only. created with aspose.words. copyright 2003-2022 aspose pty ltd.':
                            continue
                        elif re.findall(w1, line1):
                            Count += line1.count(w1)
                        if Count!=0:
                            with open("D:/Dataset/Cache/" + file_name[11:] + '.html', mode='wt', encoding='utf-8') as f:
                                f.write(line1.replace(w, '<span><mark>{}</mark></span>'.format(w)))
                    final_path = file_name
            if Count != 0:
                links[file_name] = Count
    time2 = time.time()
    print("Total Time Taken: ", time2 - time1)
    print(links)
    return links

