import time

text = input("Please enter text: ")
import os

current_path = os.getcwd()
path = 'D:/'


def searchText(path):
    os.chdir(path)
    files = os.listdir()
    for file_name in files:
        abs_path = os.path.abspath(file_name)

        if os.path.isdir(abs_path):
            searchText(abs_path)

        if os.path.isfile(abs_path):
            print(abs_path)
            if (".txt" in abs_path):
                with open(file_name, 'r', encoding='utf-8') as f:
                    if text in f.read():
                        final_path = os.path.abspath(file_name)
                        print(text + " word found in this path " + final_path)
    pass


t1 = time.time()
searchText(path)
t2 = time.time()
print("%.8f" % (t2 - t1))