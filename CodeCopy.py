import time
import os
import cv2
import pytesseract
import re
import fitz

def searchtext(keyword):
    time1 = time.time()
    root = 'D:\\dataset'
    filenames = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            filenames.append(os.path.join(path, name))
    t1 = time.time()
    for file_name in filenames:
        if(".txt" in file_name):
            with open(file_name, 'r', encoding='utf-8') as f:
                data = f.read().casefold()
                words = keyword.casefold().split()
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
                data = f.read().casefold()
                words = keyword.casefold().split()
                for w in words:
                    if w in data:
                        Count = data.count(w)
                        final_path = file_name
                        print(w," word found ",Count,"times in this path ",final_path)
    t2 = time.time()
    print("time taken for document files", t2 - t1)
    t1 = time.time()
    for file_name in filenames:
        if(".jpg" in file_name or ".png" in file_name or ".jpeg" in file_name or ".jfif" in file_name or ".tiff" in file_name
        or ".svg" in file_name):
            img = cv2.imread(file_name)
            custom_config = r'--oem 3 --psm 6'
            data=pytesseract.image_to_string(img, config=custom_config).casefold()
            words = keyword.casefold().split()
            for w in words:
                if w in data:
                    Count = data.count(w)
                    final_path = file_name
                    print(w," word found ",Count,"times in this path ",final_path)
    t2 = time.time()
    print("time taken for image files", t2 - t1)
    t1 = time.time()
    for file_name in filenames:
        if(".pdf" in file_name):
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
                        if(re.findall(w1, line1)):
                            Count += line1.count(w1)
            if Count != 0:
                final_path = file_name
                print(w," word found ",Count,"times in this path ",final_path)
    t2 = time.time()
    print("time taken for pdf files", t2 - t1)
    time2 = time.time()
    print("Total Time Taken: ", time2 - time1)
    pass

searchtext("smile")

